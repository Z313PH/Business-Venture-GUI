from tkinter import *

class BusinessVenture:
    def __init__(self):
        self.window = Tk()
        self.window.title("Business venture")
        
        # initial capital investment
        capital_label = Label(self.window, text="Enter amount of initial Capital Investment: $")
        capital_label.grid(column=0, row=0)
        self.initial_capital_investment = DoubleVar()
        capital_entry = Entry(self.window, textvariable=self.initial_capital_investment)
        capital_entry.grid(column=1, row=0)

        # monthly location expenditures
        location_label = Label(self.window, text="Enter the Monthly Location Lease Costs: $")
        location_label.grid(column=0, row=1)
        self.location_lease_costs = DoubleVar()
        location_entry = Entry(self.window, textvariable=self.location_lease_costs)
        location_entry.grid(column=1, row=1)

        utilities_label = Label(self.window, text="Enter the Monthly Location Utilities Costs: $" )
        utilities_label.grid(column=0, row=2)
        self.location_utilities_costs = DoubleVar()
        utilities_entry = Entry(self.window, textvariable=self.location_utilities_costs)
        utilities_entry.grid(column=1, row=2)

        # monthly employee expenditures
        employees_label = Label(self.window, text="How many employees do you have:")
        employees_label.grid(column=0, row=4)
        self.employees = DoubleVar()
        employees_entry = Entry(self.window, textvariable=self.employees)
        employees_entry.grid(column=1, row=4)

        payrate_label = Label(self.window, text="What is their hourly pay rate: $")
        payrate_label.grid(column=0, row=5)
        self.payrate = DoubleVar()
        payrate_entry = Entry(self.window, textvariable=self.payrate)
        payrate_entry.grid(column=1, row=5)

        hours_label = Label(self.window, text="How many hours a week do they work: ")
        hours_label.grid(column=0, row=6)
        self.hours = DoubleVar()
        hours_entry = Entry(self.window, textvariable=self.hours)
        hours_entry.grid(column=1, row=6)

        # total monthly unit sales
        sales_label = Label(self.window, text="Enter Total Monthly Unit Sales: ")
        sales_label.grid(column=0, row=9)
        self.total_monthly_unit_sales = DoubleVar()
        sales_entry = Entry(self.window, textvariable=self.total_monthly_unit_sales)
        sales_entry.grid(column=1, row=9)

               
        # Create button to calculate business venture and display results
        calc_button = Button(self.window, text="Calculate Business Venture", command=self.calculate)
        calc_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

        # Create labels to display results
        Label(self.window, text="Monthly Employee Expenditures: $").grid(column=0, row=11)
        self.monthly_employee_expenditures_label = Label(self.window, text=self.get_monthly_employee_expenditures())
        self.monthly_employee_expenditures_label.grid(column=1, row=11)

        Label(self.window, text="Monthly location expenditures: $" ).grid(row=12, column=0, pady=15)
        self.monthly_location_expenditures_label = Label(self.window, text=self.get_monthly_location_expenditures())
        self.monthly_location_expenditures_label.grid(row=12, column=1, pady=15)
        
        # monthly operational expenditures
        Label(self.window, text="Monthly Operational Expenditures: $").grid(row=13, column=0, pady=15)
        self.monthly_operational_expenditures_label = Label(self.window, text=self.get_monthly_operational_expenditures())
        self.monthly_operational_expenditures_label.grid(row=13, column=1, pady=15)

        Label(self.window, text="Coverage (in months): ").grid(row=14, column=0, pady=15)
        self.coverage_label = Label(self.window)
        self.coverage_label.grid(row=14, column=1, pady=15)

        Label(self.window, text="Business Venture: ").grid(row=15, column=0, pady=15)
        self.venture_label = Label(self.window)
        self.venture_label.grid(row=15, column=1, pady=15)

        self.window.mainloop()

    def calculate(self):
        # Get input values from GUI fields  
        initial_capital_investment = self.initial_capital_investment.get()
        monthly_location_expenditures = float(self.get_monthly_location_expenditures())
        monthly_employee_expenditures = float(self.get_monthly_employee_expenditures())
        monthly_operational_expenditures = float(self.get_monthly_operational_expenditures())
        total_monthly_unit_sales = self.total_monthly_unit_sales.get()

        # Calculate coverage and business venture
        coverage = float(initial_capital_investment) / (monthly_operational_expenditures)
        business_venture = float(total_monthly_unit_sales * coverage) - (initial_capital_investment)

        # Update GUI labels with results
        self.monthly_operational_expenditures_label.config(text="{:.2f}".format(monthly_operational_expenditures))
        self.monthly_location_expenditures_label.config(text="{:.2f}".format(monthly_location_expenditures))
        self.monthly_employee_expenditures_label.config(text="{:.2f}".format(monthly_employee_expenditures))
        self.coverage_label.config(text="{:.2f}".format(coverage))
        self.venture_label.config(text="{:.2f}".format(business_venture))


    def get_monthly_location_expenditures(self):
        monthly_location_expenditures = self.location_lease_costs.get() + self.location_utilities_costs.get()
        return monthly_location_expenditures

    def get_monthly_employee_expenditures(self):
        monthly_employee_expenditures = ((self.employees.get() * self.payrate.get() * self.hours.get()) * 52) / 12
        return monthly_employee_expenditures
    
    def get_monthly_operational_expenditures(self):
        monthly_location_expenditures = self.get_monthly_location_expenditures()
        monthly_employee_expenditures = self.get_monthly_employee_expenditures()
        monthly_operational_expenditures = monthly_location_expenditures + monthly_employee_expenditures
        return monthly_operational_expenditures


BusinessVenture()