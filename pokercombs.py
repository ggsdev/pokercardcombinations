import numpy

arrayt=[102,103,104,105,106,107,108,109,110,111,112,113,114,202,203,204,205,206,207,208,209,210,211,212,213,214,302,303,304,305,306,307,308,309,310,311,312,313,314,402,403,404,405,406,407,408,409,410,411,412,413,414]

conn=sqlite3.connect('tables.db')
c=conn.cursor()
pos1=0
pos2=1
pos3=2
pos4=3
pos5=4
pos6=5
pos7=6
i=0
while pos1<=45:
    
    while pos2<=46:
        
        while pos3<=47:  
                
            while pos4<=48: 
                
                while pos5<=49:     
                    
                    while pos6<=50: 
                        
                        while pos7<=51: 
                            c.execute("INSERT INTO TABLE2 VALUES (?, ?, ?, ?, ?, ?, ?)", ((arrayt[pos1]),(arrayt[pos2]),(arrayt[pos3]),(arrayt[pos4]),(arrayt[pos5]),(arrayt[pos6]),(arrayt[pos6])))    
                            pos7+=1
                            i+=1
                        pos6+=1
                        pos7=pos6+1
                    pos5+=1
                    pos6=pos5   
                pos4+=1
                pos5=pos4
            pos3+=1
            pos4=pos3     
        pos2+=1
        pos3=pos2
    pos1+=1
    pos2=pos1
conn.commit()
conn.close()
No comments: Links to this post 
