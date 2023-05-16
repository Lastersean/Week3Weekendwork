class Buystuff():
    
    def __init__(self ):

        self.income_1 = 0
        self.expenses_1 = 0
        # self.close_cost = close_cost
  
    def income(self):
        answer = int(input('Please enter the amount of your total income  '))
        self.income_1 = answer
        self.income_1 += 1
        

    def expenses(self):
        answer_2 = int(input('What is the amount of your total expenses?  '))
        self.expenses_1 = answer_2
        self.expenses_1 += 1
        
      
    def cash_flow(self):
        casher = self.income_1 - self.expenses_1
        print(f'Based on what you entered, your current montly cash flow is ${casher} ')

    def roi(self):
        anual_cashflow =  (self.income_1 - self.expenses_1) * 12
        print(f'Your anual cashflow is ${anual_cashflow}')
        investment = int(input('What was the amount of your total investment?  '))
        ann_roi = (investment/anual_cashflow) * 100

        print(f'Your cash on cash ROI is {ann_roi}%')

    def runner(self):
        active = True
        while active:
            answer_3 = input('Would you like to enter your income(i)  \n enter your expenses(e)   \nsee your montly cashflow(c)   \nsee your annual cashflow(a)  \n or see your cash on cash ROI(r)  ').lower()
            if answer_3 == 'i':
                Rental.income()
                
            
            elif answer_3 == 'e':
                Rental.expenses()
            
            elif answer_3 =='c':
                Rental.cash_flow()

            elif answer_3 == 'a':
                anual_cashflow =  (self.income_1 - self.expenses_1) * 12
                print(anual_cashflow)
            
            elif answer_3 == 'r':
                Rental.roi()
        
        

Rental = Buystuff()
Rental.runner()
# Rental.income()
# Rental.expenses()
# Rental.cash_flow()
# Rental.roi()


        
