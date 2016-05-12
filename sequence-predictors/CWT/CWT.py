## calculating a and b values

# i have sequence of D bits, I need to build a tree.
# I take the last D bits and treat them
#

import random

class CWT_Expert(object):
    def __init__(self,depth,alpha):
        self.depth = depth
        self.tree = CWT(depth,alpha)
        #self.last_prediction = 0;
        self.computer_score = self.player_score = 0
        self.context = [];
        self.prediction = self.get_prediction();

    def take_turn(self,player_choice):
        if player_choice == self.prediction:
            self.computer_score +=1
        else:
            self.player_score +=1

        self.context.append(player_choice)
        self.context = self.context[-self.depth:]
        self.tree.add_bit(player_choice,self.context)
        self.prediction = self.get_prediction();

    def get_prediction(self):
        prob = self.tree.predict_bit_probability(self.context)
        if random.random() >prob:
            return 0
        else:
            return 1

    
    def score(self):
        return "Computer {}, Player {}".format(self.computer_score, self.player_score)
    def flip(self):
        if random.random() > 0.5:
            return 1
        else:
            return 0
    

class Node():
    
    def __init__(self):
        
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.a = 0
        self.b = 0
        self.isRightChild = False

    def add_index(self, i):
        if i==1:
            self.b +=1
        else:
            self.a +=1

    def calculate_probability(self):
        return (self.a+0.5)/(self.a+self.b+1)


    def set_left_child(self,nodeL):
        self.leftChild = nodeL
        nodeL.set_parent(self)

    def set_right_child(self,nodeR):
        self.rightChild = nodeR
        self.rightChild.isRightChild = True
        nodeR.set_parent(self)

    def set_parent(self,nodeP):
        self.parent = nodeP

#assumption: context is length D


class CWT():

    def __init__(self, d, alpha):
        self.root = Node()
        self.depth = d
        self.alpha = alpha
        self.expand_node(self.root,0)

    def expand_node(self,node, currentDepth):
        if currentDepth < self.depth:
            node.set_left_child(Node())
            node.set_right_child(Node())
            self.expand_node(node.leftChild,currentDepth +1)
            self.expand_node(node.rightChild,currentDepth +1)    

    def add_bit(self,bit, context):
        node = self.root
        for i in range(0,len(context)):
            node.add_index(bit)
            if context[-i-1] ==0:
                node = node.leftChild
            else:
                node = node.rightChild
                
        node.add_index(bit)
        

    def predict_bit_probability(self,context):
        probs_0 = [self.root.calculate_probability()];
        node = self.root;
        for i in range(0,len(context)):
            if context[-i-1] ==0:
                node = node.leftChild
            else:
                node = node.rightChild
            probs_0.append(node.calculate_probability())

        return sum(self.alpha**k*probs_0[k] for k in range(len(probs_0)))/sum(self.alpha**k for k in range(len(probs_0)));


######################## USE CASES ###########################
##depth = 5;
##alpha = 5
##CWT_new = CWT_Expert(depth,alpha)
##
##
##while True:
##    bit = int(raw_input("please enter number :  "))
##    print CWT_new.prediction
##    CWT_new.take_turn(bit)


## evaluating losses

    
    
