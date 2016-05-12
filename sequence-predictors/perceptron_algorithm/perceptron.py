import numpy as np

class Perceptron(object):
    def __init__(self,window,alpha):
        self.window = window
        self.alpha = alpha
        #self.x = np.ones([window,1])
        self.x = [0.5]*window
        self.w = np.ones([1,window])
        self.w_0 =0
        self.prediction = self.get_prediction();
        #self.last_prediction = 0;
        self.computer_score = self.player_score = 0

    def take_turn(self,player_choice):
        if player_choice == self.prediction:
            self.computer_score +=1
        else:
            self.player_score +=1
            self.update_weights(player_choice);

        self.x.append(player_choice)
        self.x = self.x[-self.window:]
        self.prediction = self.get_prediction();

    def get_prediction(self):
        pred = np.dot(self.w,np.transpose(np.matrix(self.x)))+self.w_0;
        #print pred
        if pred >0:
            return 1
        else:
            return 0
        
    def update_weights(self,player_choice):
        y = 1
        if player_choice ==0:
            y=-1
            
        self.w += self.alpha*np.matrix(self.x)*y
        #print self.w
        self.w_0 += self.alpha*y

    
    def score(self):
        return "Computer {}, Player {}".format(self.computer_score, self.player_score)
    def flip(self):
        if random.random() > 0.5:
            return 1
        else:
            return 0

#### try it out
##alpha = 0.1
##window =3
##
##p = Perceptron(window,alpha)
##
##while True:
##    human = float(raw_input("please enter number : "))
##    print p.prediction
##    p.take_turn(human)
