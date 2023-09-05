from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class InstrScr(Screen):
    def __init__(self, name = 'inst', **kwargs):
        super().__init__(name=name, **kwargs)
        txt = Label(text =  '''
Ця програма дозволить вам за допомогою тесту Руфьє здійснити першинну діагностику вашого здоров'я.\n
Тест Руфьє - це навантажувальний комплекс, створений для оцінки працездатності серця при фізичному навантаженні.
У досліджуваного визначають частоту пульсу протягом 15 секунд.
Потім протягом 45 секунд досліджуваний виконує 30 присідань.\n
Після завершення навантаження пульс знову підраховується: кількість пульсацій за перші 15 секунд, 30 секунд відпочинку,\n кількість пульсацій за останні 15 секунд.''', size_hint=(1,.7))
        txt1 = Label(text = "Введіть ім'я: ")
        txt2 = Label(text = 'Введіть вік: ')
        self.text_input1 = TextInput(multiline = False, size_hint=(.8,.5))
        self.text_input2 = TextInput(text = '0', multiline = False, size_hint=(.8,.5))
        btn = Button(text = 'Почати', size_hint=(.3,.1), pos_hint = {'center_x': 0.5})
        btn.on_press = self.next
        layout = BoxLayout(orientation = 'vertical', padding = 4, spacing = 8)
        layout1 = BoxLayout(orientation = 'horizontal', size_hint=(1,.1))
        layout2 = BoxLayout(orientation = 'horizontal',size_hint=(1,.1))
        layout1.add_widget(txt1)
        layout1.add_widget(self.text_input1)
        layout2.add_widget(txt2)
        layout2.add_widget(self.text_input2)
        layout.add_widget(txt)
        layout.add_widget(layout1)
        layout.add_widget(layout2)
        layout.add_widget(btn)
        self.add_widget(layout)

    def next(self):
        global name, age
        name = self.text_input1.text
        age = int(self.text_input2.text)

        self.manager.transition.direction = 'left'
        self.manager.current = 'pulse1'

    
class PulseScr(Screen):
    def __init__(self, name = 'pulse1'):
        super().__init__(name=name)
        txt1 = Label(text= '''
Виміряйте пульс протягом 15 секунд.
Результат запишіть у відповідне поле.
''', size_hint=(1,.7))
        txt2 = Label(text = 'Введіть результат: ')
        self.text_input = TextInput(text = '0', multiline = False, size_hint=(.8,.55))
        btn = Button(text = 'Продовжити', size_hint=(.5,.125), pos_hint = {'center_x': 0.5})
        btn.on_press = self.next
        layout = BoxLayout(orientation = 'vertical', padding = 4, spacing = 8)
        layout1 = BoxLayout(orientation = 'horizontal', size_hint=(1,.075))
        layout1.add_widget(txt2)
        layout1.add_widget(self.text_input)
        layout.add_widget(txt1)
        layout.add_widget(layout1)
        layout.add_widget(btn)
        self.add_widget(layout)

    def next(self):
        global P1
        P1 = self.text_input.text
        self.manager.transition.direction = 'left'
        self.manager.current = 'check1'



class CheckSits(Screen):
    def __init__(self, name = 'check1'):
        super().__init__(name=name)
        txt = Label(text = 'Виконайте 30 присідань протягом 45 секунд.', size_hint=(1,.8))
        btn = Button(text = 'Продовжити', size_hint=(.5,.2), pos_hint = {'center_x': 0.5})
        layout = BoxLayout(orientation = 'vertical', padding = 30, spacing = 8)
        layout.add_widget(txt)
        layout.add_widget(btn)
        self.add_widget(layout)
        btn.on_press = self.next
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'pulse2'


class PulseScr2(Screen):
    def __init__(self, name = 'pulse2'):
        super().__init__(name=name)



        txt = Label(text =  '''Протягом хвилини виміряйте пульс двічі:\n 
за перші 15 секунд хвилини, а потім за останні 15 секунд.\n
Результати запишіть у відповідні поля.''', size_hint=(1,.7))
        txt1 = Label(text = "Результат: ")
        txt2 = Label(text = 'Результат після відпочинку: ')
        self.text_input1 = TextInput(text = '0', multiline = False, size_hint=(.8,.5))
        self.text_input2 = TextInput(text = '0', multiline = False, size_hint=(.8,.5))
        btn = Button(text = 'Завершити', size_hint=(.3,.1), pos_hint = {'center_x': 0.5})
        btn.on_press = self.next
        layout = BoxLayout(orientation = 'vertical', padding = 4, spacing = 8)
        layout1 = BoxLayout(orientation = 'horizontal', size_hint=(1,.1))
        layout2 = BoxLayout(orientation = 'horizontal',size_hint=(1,.1))
        layout1.add_widget(txt1)
        layout1.add_widget(self.text_input1)
        layout2.add_widget(txt2)
        layout2.add_widget(self.text_input2)
        layout.add_widget(txt)
        layout.add_widget(layout1)
        layout.add_widget(layout2)
        layout.add_widget(btn)
        self.add_widget(layout)




    def next(self):
        global P2, P3
        P2 = self.text_input1.text
        P3 = self.text_input2.text
        app.result_screen.add1()
        self.manager.transition.direction = 'left'
        self.manager.current = 'result'



class Result(Screen):
    def __init__(self, name = 'result', **kwargs):
        super().__init__(name=name, **kwargs)
        self.txt = Label(text='')
        self.add_widget(self.txt)
    def add1(self):
        index1 =  (4 *(int(P1) + int(P2) + int(P3)) - 200)/10
        if age >= 15:
            if index1 >= 15:
                index2 = 'Низький'
            elif index1 >= 11 and index1 <= 14.9:
                index2 = 'Задоволений'
            elif index1 >= 6 and index1 <= 10.9:
                index2 = 'Середній'
            elif index1 >= 0.5 and index1 <= 5.9:
                index2 = 'Вище середнього'
            else:
                index2 = 'Високий'
        elif age >= 13 and age <= 14:
            if index1 >= 16.5:
                index2 = 'Низький'
            elif index1 >= 12.5 and index1 <= 16.4:
                index2 = 'Задоволений'
            elif index1 >= 7.5 and index1 <= 12.4:
                index2 = 'Середній'
            elif index1 >= 2 and index1 <= 7.4:
                index2 = 'Вище середнього'
            else:
                index2 = 'Високий'
        elif age >= 11 and age <= 12:
            if index1 >= 18:
                index2 = 'Низький'
            elif index1 >= 14 and index1 <= 17.9:
                index2 = 'Задоволений'
            elif index1 >= 9 and index1 <= 13.9:
                index2 = 'Середній'
            elif index1 >= 3.5 and index1 <= 8.9:
                index2 = 'Вище середнього'
            else:
                index2 = 'Високий'
        elif age >= 9 and age <= 10:
            if index1 >= 19.5:
                index2 = 'Низький'
            elif index1 >= 15.5 and index1 <= 19.4:
                index2 = 'Задоволений'
            elif index1 >= 10.5 and index1 <= 15.4:
                index2 = 'Середній'
            elif index1 >= 5 and index1 <= 10.4:
                index2 = 'Вище середнього'
            else:
                index2 = 'Високий'
        else:
            if index1 >= 21:
                index2 = 'Низький'
            elif index1 >= 17 and index1 <= 20.9:
                index2 = 'Задоволений'
            elif index1 >= 12 and index1 <= 16.9:
                index2 = 'Середній'
            elif index1 >= 6.5 and index1 <= 11.9:
                index2 = 'Вище середнього'
            else:
                index2 = 'Високий'
        try:
            self.txt.text = (f"{str(name)}\nВаш індекс Руф'є: {str(index1)}\nПрацездатність серця: {str(index2)}")
        except Exception:
            self.txt.text = ('Ви ввели некоректні данні')


sm = ScreenManager()
sm.add_widget(InstrScr(name='instr'))
sm.add_widget(PulseScr(name='pulse1'))
sm.add_widget(CheckSits(name='check1'))
sm.add_widget(PulseScr2(name='pulse2'))
class HeartCheck(App):
    def build(self):
        Window.size = (900, 700)
        Window.position = 'custom'
        Window.left = 500
        Window.top = 188
        self.screen_manager = sm
        self.result_screen = Result(name='result')                  
        sm.add_widget(self.result_screen)

        return sm
app = HeartCheck()
app.run()