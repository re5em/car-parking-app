import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

file = "parking.json"

if os.path.exists(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    data = {}

class ParkingApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        layout.add_widget(Label(text="PARKING SYSTEM", font_size=24))
        
        # Search by car number
        layout.add_widget(Label(text="Car Number:"))
        self.car_input = TextInput(hint_text="Enter car number", multiline=False)
        layout.add_widget(self.car_input)
        
        btn_car = Button(text="Search by Car")
        btn_car.bind(on_press=self.search_by_car)
        layout.add_widget(btn_car)
        
        # Search by house number
        layout.add_widget(Label(text="House Number:"))
        self.house_input = TextInput(hint_text="Enter house number", multiline=False)
        layout.add_widget(self.house_input)
        
        btn_house = Button(text="Search by House")
        btn_house.bind(on_press=self.search_by_house)
        layout.add_widget(btn_house)
        
        # Add new
        layout.add_widget(Label(text="--- ADD NEW ---"))
        self.new_car = TextInput(hint_text="New car number", multiline=False)
        layout.add_widget(self.new_car)
        self.new_house = TextInput(hint_text="New house number", multiline=False)
        layout.add_widget(self.new_house)
        
        btn_add = Button(text="ADD", background_color=[0,1,0,1])
        btn_add.bind(on_press=self.add)
        layout.add_widget(btn_add)
        
        # Result
        self.result = Label(text="Result here", size_hint_y=None, height=100)
        layout.add_widget(self.result)
        
        btn_show = Button(text="Show All")
        btn_show.bind(on_press=self.show_all)
        layout.add_widget(btn_show)
        
        return layout
    
    def search_by_car(self, instance):
        car = self.car_input.text.strip()
        if car in data:
            self.result.text = f"House: {data[car]}"
        else:
            self.result.text = "Not found"
    
    def search_by_house(self, instance):
        house = self.house_input.text.strip()
        results = [c for c, h in data.items() if h == house]
        if results:
            self.result.text = f"Cars: {', '.join(results)}"
        else:
            self.result.text = "Not found"
    
    def add(self, instance):
        car = self.new_car.text.strip()
        house = self.new_house.text.strip()
        if car and house:
            data[car] = house
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self.result.text = f"Saved: {car} -> {house}"
            self.new_car.text = ""
            self.new_house.text = ""
        else:
            self.result.text = "Fill all fields"
    
    def show_all(self, instance):
        if data:
            text = "DATA:\n"
            for c, h in data.items():
                text += f"{c} -> {h}\n"
            self.result.text = text
        else:
            self.result.text = "No data"

if __name__ == "__main__":
    ParkingApp().run()