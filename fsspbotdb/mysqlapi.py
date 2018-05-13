import configparser
from mysql import connector
class MyTable():
    def add(self,*args,**kwargs):
 
    #INSERT INTO dept VALUES (50, «ПРОДУКЦИЯ», «САН-ФРАНЦИСКО»);
    #INSERT INTO Customers (city, cname, cnum) VALUES (‘London’, ‘Hoffman’, 2001);
        ff='INSERT INTO '+ self.table_name+' ('+  ', '.join(kwargs.keys() ) + ') VALUES ('+  ', '.join(kwargs.values() ) + ')'
        print (ff)
    def update(self,*args,**kwargs):
        ff=' where '+ ' and '.join(k+'='+str(v) for (k,v) in self._filter.items() )
        itms= ', '.join('set '+k+'='+str(v) for (k,v) in kwargs.items() ) 
        sq='update '+ self.table_name +' '+itms+' '+ff
        print (sq)
    def save(self):
        self.conn.commit()
    def values (self,*args,**kwargs):
        if self._filter =={}  :
            ff=''
        else:
            ff=' where '+ ' and '.join(k +'='+str(v) for (k,v) in self._filter.items() )
        if len(args)==0:
            sq='select * from '+self.table_name +ff
        else:
            sq='select ' +', '.join(args) +' from '+self.table_name  +ff
        self.cursor.execute (sq)
        return self.cursor.fetchall()
        
    def filter(self,*args,**kwargs):
        print (kwargs)
        self._filter=dict(kwargs)
    def __init__(self,conn,table_name,prefix):
        self._filter={}
        self.conn=conn
        self.cursor = self.conn.cursor()
        self.table_name=prefix+table_name
        
class MyData():
    def get_table (self,table_name):
        return MyTable(self.conn,table_name, self.table_prefix)
    def __init__(self,config_file):
        config=configparser.ConfigParser()
        config.read(config_file)
        client=config['client']
        self.conn=connector.connect(host                  = 'localhost',
                           database              = client['database'],
                           user                  = client['user'],
                           password              = client['password'])
        #self.cursor = self.conn.cursor()
        self.table_prefix= client['prefix']    
    def __del__(self):
        self.conn.close()