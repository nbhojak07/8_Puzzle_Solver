# -*- coding: utf-8 -*-
"""Proj1_Nidhi_Bhojak.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qIghHHJcTRGx8UVX9eZrBDD0d4_gltPS
"""

import numpy as np
  import itertools

  #Taking User input for the initial state
  print("Enter the first row considering the spaces:")
  a=[int(x) for x in input().split()]
  print("Enter the second row considering the spaces")
  b=[int(x) for x in input().split()]
  print("Enter the second row considering the spaces")
  c=[int(x) for x in input().split()]
  

  Input_Node= np.vstack((a,b,c))
  Goal_Node= np.array([[1,2,3],[4,5,6],[7,8,0]])

  #Checking whether the solution to the state exists or not
  def Is_Valid(node):
    x=node.ravel()
    x=x.tolist()
    x=[a for a in x if a!=0]
    count=0
    for i in range(0, len(x)):
      y=x[i]
      c=0
      for j in range(i,len(x)):
        if x[j]<y:
          c=c+1
      count=count+c
    if count%2==0:
      return True
    else: 
      return False


  #Function to convert 3*3 matrix into a string form
  def Node_Str(J):
    chain= list(itertools.chain(*J))
    G = ' '.join(map(str,chain))
    return G
  

  Input_Str=Node_Str(Input_Node)
  Final_Str= Node_Str(Goal_Node)


  #Function to locate the zero in the array
  def Find_zero(node):
    for x in range(0,3):
      for y in range (0,3):
        if(node[x][y]==0):
          return x,y


  #Function to move the zero in left direction
  def Move_left(node):
    x,y= Find_zero(node)
    if y==0:
      flag= 1
      return flag
    else:
      temp_node=np.copy(node)
      temp_node[x][y]=temp_node[x][y-1]
      temp_node[x][y-1]=0
      flag=0
      return temp_node

      
    
  
  
  #Function to mov zero in right direction
  def Move_right(node):
    x,y= Find_zero(node)
    if y==2:
      flag=1
      return flag
    else:
      temp_node=np.copy(node)
      temp_node[x][y]=temp_node[x][y+1]
      temp_node[x][y+1]=0
      flag=0
      return temp_node
    
    

  
  #Function to move zero in Up direction
  def Move_up(node):
    x,y= Find_zero(node)
    if x==0:
      flag=1
      return flag

    else:
      temp_node=np.copy(node)
      temp_node[x][y]=temp_node[x-1][y]
      temp_node[x-1][y]=0
      flag=0
      return temp_node
    
    

  
  #Function to move zero in Down direction
  def Move_down(node):
    x,y= Find_zero(node)
    if x==2:
      flag=1
      return flag
      
    else:
      temp_node=np.copy(node)
      temp_node[x][y]=temp_node[x+1][y]
      temp_node[x+1][y]=0
      flag=0
      return temp_node
    
    

  if(Is_Valid(Input_Node)==False):
    print("The solution does not exist, try rearranging the numbers")

  elif(Input_Str==Final_Str):
    print("The initial and final states are the same")

  else:
    loc=[]
    Node_Visited=[]
    Node_Visited.append(Input_Node)
    Node_info=[]
    i=0
    j=1
    
    goal=0
    k=0

    Node_info.append(Input_Str)


    while 1:
      
      #Checking for the new generated nodes in all four actions and appending them 
      if(goal==1):
        break
      else:
        p=np.array(Node_Visited[i])
        q=np.array(Move_left(p))
        if(np.shape(q)!=(3,3)):
          k=1
        else:
          n=Node_Str(q)
          check=0
          for a in range(0,len(Node_info)):
            if(n==Node_info[a]):
              check=1
          if(check!=1):
            Node_Visited.append(q)
            Node_info.append(n)
            l1=[i,j]
            loc.append(l1)
            j=j+1
          if(n==Final_Str):
            goal=1
            
    
      

      if(goal==1):
        break
      else:
        s=np.array(Node_Visited[i])
        q=np.array(Move_up(s))
        if(np.shape(q)!=(3,3)):
          k=1
        else:
          n= Node_Str(q)
          check=0
          for c in range(0,len(Node_info)):
            if(n==Node_info[c]):
              check=1
          if(check!=1):
            Node_Visited.append(q)
            Node_info.append(n)
            l3=[i,j]
            loc.append(l3)
            j=j+1
          if(n==Final_Str):
            goal=1
        

      if(goal==1):
        break
      else:
        r=np.array(Node_Visited[i])
        q=np.array(Move_right(r))
        if(np.shape(q)!=(3,3)):
          k=1
        else:
          n=Node_Str(q)
          check=0
          for b in range(0,len(Node_info)):
            if(n==Node_info[b]):
              check=1
          if(check!=1):
            Node_Visited.append(q)
            Node_info.append(n)
            l2=[i,j]
            loc.append(l2)
            j=j+1
          if(n==Final_Str):
            goal=1
        

      if(goal==1):
        break
      else:
        t=np.array(Node_Visited[i])
        q=np.array(Move_down(t))
        if(np.shape(q)!=(3,3)):
          k=1
        else:
          n= Node_Str(q)
          check=0
          for d in range(0,len(Node_info)):
            if(n==Node_info[d]):
              check=1
          if(check!=1):
            Node_Visited.append(q)
            Node_info.append(n)
            l4=[i,j]
            loc.append(l4)
            j=j+1
          if(n==Final_Str):
            goal=1
      
      i=i+1

    
    l=len(loc)-1
    order=[]
    
    #Appending address of the last element
    order.append(loc[l][1])
    order.append(loc[l][0])
    k=loc[l][0]

    #Checking for the Parent Node of the Corresponding Child Node
    for a in range(0, len(loc)-1):
      for b in range(0, len(loc)):
        if loc[b][1]==k:
          order.append(loc[b][0])
          k= loc[b][0]
                    

    order=order[::-1] #Reversing the order of the final path
    final_path=[]
    for f in order:
      final_path.append(Node_Visited[f])

    for t in range(0,len(final_path)):
      print(final_path[t])

    
out_file = open("Node_info.txt", 'w')
  for x in Node_info:
    out_file.write(str(Node_info) + '\n')
  out_file.close()

out_file = open("final_path.txt", 'w')
  for x in final_path:
    out_file.write(str(final_path) + '\n')
  out_file.close()
    
    
out_file = open("NodesAll.txt", 'w')
  for x in order:
    out_file.write(str(order) + '\n')
  out_file.close()