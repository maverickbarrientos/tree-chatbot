import json

try:
  with open("data.json", "r", encoding="utf-8") as file:
    story_tree = json.load(file)
except Exception as e:
  print(f"Error : {e}")
  
class Node():
    def __init__(self, question, choices, result=None):
        self.question = question
        self.choices = choices or []
        self.result = result
        
    def terminal_open(self):
        return self.result is None
    
    def display_node(self):
        print("=========================")
        print(self.question)
        for choice in self.choices:
            print(choice["label"]) 
                
class Chatbot():
    def __init__(self, tree):
        self.tree = tree
        self.node = None
        self.current_node = None
        
    def start(self):
        self.current_node = self.tree["start"]    
        
def compare_input(user_input, choices):
    for choice in choices:
        label = choice["label"].lower()
        if user_input == label.split(".")[0].strip() or user_input.lower() in label:
            return choice["next"]
        
bot = Chatbot(story_tree)

bot.start()

current_node = bot.current_node
node = Node(current_node["question"], current_node["choices"])
selected_choice = None

while node.terminal_open():
    
    node.display_node()
        
    choice = input("> ")
    selected_choice = compare_input(choice, node.choices)
        
    if selected_choice:
        current_node = bot.tree[selected_choice]
        result = current_node.get("result", None)
        
        if result:
            print(f"Genre : {result}")
            print(f"Story Recommendation : {current_node["story"]}")
            break
            
        node = Node(current_node["question"], current_node["choices"], result)
    else:
        print("INVALID INPUT!")
