class frac:
    def __init__(self, inp):
        """
        This function is used to initialize a fraction.
        Example:
            frac("1/2")
        Here 1 will be the numerator and 2 will be the denominator
        """
        if isinstance(inp, str):     #check if input in bracket is a string
            nums = inp.split("/")       #split the numerator and denominator
            if len(nums) == 2:          #Check if it isn't like 2/2/2
                sign1, sign2 = 1, 1         #Changing signs
                if nums[0][0] == "-":
                    nums[0] = nums[0][1:]       #Remove the sign from the number
                    sign1 = -1
                if nums[1][0] == "-":
                    nums[1] = nums[1][1:]
                    sign2 = -1
                if nums[0][0] == "+":
                    nums[0] = nums[0][1:]
                if nums[1][0] == "+":
                    nums[1] = nums[1][1:]
                    
                if sign1 == -1 and sign2 == -1:
                    sign1, sign2 = 1, 1
                
                for i in range(len(nums)):
                    if nums[i].isdigit():       #Check if the input is a number not like 2#2
                        continue
                    else:
                        print("Digits only")
                        break
                else:       #The numerator and denominator are numbers
                    self.__up = sign1 * sign2 * int(nums[0])  #Changing sign of fraction
                    self.__down = int(nums[1])  
                    frac.__simplfy(self)    #simplifying the fraction
            else:
                print("Incorrect format")
        
        else:
            print("Incorrect format")
            
    def __str__(self):
        if self.__getDenom() == 1:
            if self.__up == 1:
                return str(1)
            else:
                return str(self.__up)
        else:
            return str(self.__up)+"/"+str(self.__down)
    
    def __repr__(self):
        if self.__getDenom() == 1:
            if self.__up == 1:
                return str(1)
            else:
                return str(self.__up)
        else:
            return str(self.__up)+"/"+str(self.__down)
        
    def __simplfy(self):
        """
        This function is used to simplfy the fraction to its lowest terms.
        """
        if self.__up > self.__down:
            i = self.__up
            while i >= 1:
                if self.__up%i == 0 and self.__down%i == 0:
                    self.__up = self.__up // i
                    self.__down = self.__down // i
                i = i - 1
        elif self.__down > self.__up:
            i = self.__down
            while i >= 1:
                if self.__up%i == 0 and self.__down%i == 0:
                    self.__up = self.__up // i
                    self.__down = self.__down // i
                i = i - 1
        else:
            self.__up = 1 
            self.__down = 1   
         
    def __getNum(self):
        return self.__up
    def __getDenom(self):
        return self.__down
    
    def __add__(self, other):
        """
        This fucntion is used to add a fraction with another fraction or an integer
        """
        if isinstance(other, frac):
            numer = (self.__getNum() * other.__getDenom()) + (other.__getNum() * self.__getDenom())
            denom = self.__down * other.__down
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew
        elif isinstance(other, int):
            numer = (self.__getNum() * 1) + (other * self.__getDenom())
            denom = self.__down * 1
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew
        
    def __radd__(self, other):
        """
        This function is similar to the __add__ function but this can be used to add an integer with a fraction
        """
        if isinstance(other, int):
            numer = (self.__getNum() * 1) + (other * self.__getDenom())
            denom = self.__down * 1
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew
    
    def __sub__(self, other):
        """
        This function is used to subtract a fraction and another fraction or an integer
        """
        if isinstance(other, frac):
            numer = (self.__getNum() * other.__getDenom()) - (other.__getNum() * self.__getDenom())
            denom = self.__down * other.__down
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew
        elif isinstance(other, int):
            numer = (self.__getNum() * 1) - (other * self.__getDenom())
            denom = self.__down * 1
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew
        
    def __rsub__(self, other):
        """
        This function is similar to the __sub__ function but the former can be used to subtract an integer with a fraction
        """
        if isinstance(other, int):
            numer = (other * self.__getDenom()) - (self.__getNum() * 1)
            denom = self.__down * 1
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew
    
    def __mul__(self, other):
        """
        This function is used to multiply a fraction and another fraction or an integer
        """
        if isinstance(other, frac):
            numer = self.__getNum() * other.__getNum()
            denom = self.__getDenom() * other.__getDenom()
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew
        elif isinstance(other, int):
            numer = self.__getNum() * other
            denom = self.__down
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew
        
    def __rmul__(self, other):
        """
        This function is similar to the __mul__ function but the former can be used to multiply an integer with a fraction
        """
        if isinstance(other, int):
            numer = other * self.__getNum()
            denom = self.__down 
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew    
        
    def __truediv__(self, other):
        """
        This function is used to divide a fraction and another fraction or an integer
        """
        if isinstance(other, frac):
            numer = self.__getNum() * other.__getDenom()
            denom = self.__getDenom() * other.__getNum()
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew
        elif isinstance(other, int):
            numer = self.__getNum()
            denom = self.__down * other
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew
        
    def __rtruediv__(self, other):
        """
        This function is similar to the __truedive__ function but the former can be used to divide an integer with a fraction
        """
        if isinstance(other, int):
            numer = self.__getDenom() * other
            denom = self.__getNum()
            fracNew = frac(str(numer)+"/"+str(denom))
            return fracNew   