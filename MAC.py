class MAC:

    def __init__(self,n):
        self.n=n
        self.goal=((0,0,0),(n,n,1))

    def bfs(self):
        print('\nBFS : ')
        opened,closed=[],[]
        opened.append(((self.n,self.n,1),(0,0,0)))
        print("state-x","open","close",sep='\t\t\t')
        count=0
        while opened:
            p=opened.pop(0)
            closed.append(p)
            (lm,lc,lb),(rm,rc,rb)=p
            # Goal case
            if p==self.goal:
                print('p = ',p);print('Open = ',opened);print('Close = ',closed)
                print("Success");print("Completed in ",count," steps");return
            # if boat is on left
            if lb==1:
                # Rule - 1 shift 2 missionaries
                if lm-2>=0 and (lm-2>=lc or lm-2==0) and rm+2<=3 and rm+2>=rc:
                    temp=((lm-2,lc,0),(rm+2,rc,1))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 2 shift 2 canniballs    
                if lc-2>=0 and (lm>=lc-2 or lm==0) and rc+2<=3 and (rm>=rc+2 or rm==0):
                    temp=((lm,lc-2,0),(rm,rc+2,1))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 3 shift 1 missionary and 1 canniballs    
                if lc-1>=0 and lm-1>=0 and (lm-1>=lc-1 or lm==0)  and rc+1<=3 and rm+1<=3 and rm+1>=rc+1:
                    temp=((lm-1,lc-1,0),(rm+1,rc+1,1))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 4 shift 1 canniballs    
                if lc-1>=0 and (lm>=lc-1 or lm==0) and rc+1<=3 and (rm>=rc+1 or rm==0):
                    temp=((lm,lc-1,0),(rm,rc+1,1))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 5 shift 1 missionary
                if lm-1>=0 and (lm-1>=lc or lm-1==0) and rm+1<=3 and rm+1>=rc:
                    temp=((lm-1,lc,0),(rm+1,rc,1))
                    if temp not in opened and temp not in closed:opened.append(temp)
            # if boat is on right
            else:
                # Rule - 1 shift 2 missionaries
                if rm-2>=0 and (rm-2>=rc or rm-2==0) and lm+2<=3 and lm+2>=lc:
                    temp=((lm+2,lc,1),(rm-2,rc,0))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 2 shift 2 canniballs    
                if rc-2>=0 and (rm>=rc-2 or rm==0) and lc+2<=3 and (lm>=lc+2 or lm==0):
                    temp=((lm,lc+2,1),(rm,rc-2,0))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 3 shift 1 missionary and 1 canniballs    
                if rc-1>=0 and rm-1>=0 and (rm-1>=rc-1 or lm==0) and lc+1<=3 and lm+1<=3 and lm+1>=lc+1:
                    temp=((lm+1,lc+1,1),(rm-1,rc-1,0))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 4 shift 1 canniballs    
                if rc-1>=0 and (rm>=rc-1 or rm==0) and lc+1<=3 and (lm>=lc+1 or lm==0):
                    temp=((lm,lc+1,1),(rm,rc-1,0))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 5 shift 1 missionary
                if rm-1>=0 and (rm-1>=rc or rm-1==0) and lm+1<=3 and lm+1>=lc:
                    temp=((lm+1,lc,1),(rm-1,rc,0))
                    if temp not in opened and temp not in closed:opened.append(temp)
            print('p = ',p);print('Open = ',opened);print('Close = ',closed);count+=1
        print("Goal not found")

    def dfs(self):
        print('\nDFS : ')
        opened,closed=[],[]
        opened.append(((self.n,self.n,1),(0,0,0)))
        print("state-x","open","close",sep='\t\t\t')
        count=0
        while opened:
            p=opened.pop()
            closed.append(p)
            (lm,lc,lb),(rm,rc,rb)=p
            # Goal case
            if p==self.goal:
                print('p = ',p);print('Open = ',opened);print('Close = ',closed)
                print("Success");print("Completed in ",count," steps");return
            # if boat is on left
            if lb==1:
                # Rule - 1 shift 2 missionaries
                if lm-2>=0 and (lm-2>=lc or lm-2==0) and rm+2<=3 and rm+2>=rc:
                    temp=((lm-2,lc,0),(rm+2,rc,1))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 2 shift 2 canniballs    
                if lc-2>=0 and (lm>=lc-2 or lm==0) and rc+2<=3 and (rm>=rc+2 or rm==0):
                    temp=((lm,lc-2,0),(rm,rc+2,1))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 3 shift 1 missionary and 1 canniballs    
                if lc-1>=0 and lm-1>=0 and (lm-1>=lc-1 or lm==0)  and rc+1<=3 and rm+1<=3 and rm+1>=rc+1:
                    temp=((lm-1,lc-1,0),(rm+1,rc+1,1))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 4 shift 1 canniballs    
                if lc-1>=0 and (lm>=lc-1 or lm==0) and rc+1<=3 and (rm>=rc+1 or rm==0):
                    temp=((lm,lc-1,0),(rm,rc+1,1))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 5 shift 1 missionary
                if lm-1>=0 and (lm-1>=lc or lm-1==0) and rm+1<=3 and rm+1>=rc:
                    temp=((lm-1,lc,0),(rm+1,rc,1))
                    if temp not in opened and temp not in closed:opened.append(temp)
            # if boat is on right
            else:
                # Rule - 1 shift 2 missionaries
                if rm-2>=0 and (rm-2>=rc or rm-2==0) and lm+2<=3 and lm+2>=lc:
                    temp=((lm+2,lc,1),(rm-2,rc,0))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 2 shift 2 canniballs    
                if rc-2>=0 and (rm>=rc-2 or rm==0) and lc+2<=3 and (lm>=lc+2 or lm==0):
                    temp=((lm,lc+2,1),(rm,rc-2,0))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 3 shift 1 missionary and 1 canniballs    
                if rc-1>=0 and rm-1>=0 and (rm-1>=rc-1 or lm==0) and lc+1<=3 and lm+1<=3 and lm+1>=lc+1:
                    temp=((lm+1,lc+1,1),(rm-1,rc-1,0))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 4 shift 1 canniballs    
                if rc-1>=0 and (rm>=rc-1 or rm==0) and lc+1<=3 and (lm>=lc+1 or lm==0):
                    temp=((lm,lc+1,1),(rm,rc-1,0))
                    if temp not in opened and temp not in closed:opened.append(temp)
                # Rule - 5 shift 1 missionary
                if rm-1>=0 and (rm-1>=rc or rm-1==0) and lm+1<=3 and lm+1>=lc:
                    temp=((lm+1,lc,1),(rm-1,rc,0))
                    if temp not in opened and temp not in closed:opened.append(temp)
            print('p = ',p);print('Open = ',opened);print('Close = ',closed);count+=1
        print("Goal not found")


n=int(input("Enter no.of missionaries and canniballs: "))
m=MAC(n)
m.bfs()
m.dfs()            
