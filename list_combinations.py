"""
Returns all combinations of a list
"""
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        res_list=[]
        for ing in self.ingredients:
            for top in self.toppings:
                res_list.append([ing,top])
            
        return res_list

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce", "strawberry"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]