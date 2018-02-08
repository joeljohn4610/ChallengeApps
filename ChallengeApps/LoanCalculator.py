#Declare and initialize the variables
monthlyPayment = 0
loanAmount = 0
interestRate = 0
numberOfPayments = 0
loanDurationInYears = 0

#A nice little welcome message
print('Welcome!')
print('Thank you for choosing my awesome loan calculator')

#Get inputs from user
strLoanAmount = input('Please enter your total loan amount     ')
strInterestRate = input('Please enter your interest rate, ex. .05 for 5\%     ')
strLoanDurationInYears = input('Please enter the term, in years, of your loan     ')

#Change strings from user input to float values and assign to previously declared variables
loanAmount = float(strLoanAmount)
interestRate = float(strInterestRate)
loanDurationInYears = float(strLoanDurationInYears)

#We don't want them getting impatient!
print('Thank you for this information.\n Please wait while I calculate.')

#Need to convert years the user entered to months
numberOfPayments = loanDurationInYears * 12

#Calculate the monthly payment
monthlypayment =  loanAmount * interestRate * (1 + interestRate) *  numberOfPayments \
    / ((1 + interestRate) * numberOfPayments - 1 )

#Print the monthly payment to the screen for the user
print('Your monthly payment would be {0:.2f}' .format(monthlypayment))