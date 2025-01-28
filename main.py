#source add opencv and other lib to code  : https://stackoverflow.com/questions/71184515/how-to-access-androids-camera-using-opencv-and-kivy


import kivy
from kivy.lang import Builder
kivy.require('2.1.0') # replace with your current kivy version !
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.popup import Popup
from kivy.core.image import Image as CoreImage
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.core.window import Window




import bidi.algorithm




import cv2,os,sys,arabic_reshaper  ,PIL ,winsound ,pyzbar.pyzbar 
#from pyzbar.pyzbar import decode
#import  pyzbar.pyzbar as PYZBAR
#from import Image as ImagePIL


button_argv_can_be_used = ['_animation_fade_bg', '_default_icon_color', '_default_text_color',
'_default_theme_icon_color', '_default_theme_text_color', '_disabled_color',
'_doing_ripple', '_fading_out', '_finishing_ripple', '_icon_color', '_line_color',
'_line_color_disabled', '_md_bg_color', '_md_bg_color_disabled', '_min_height', '_min_width',
'_no_ripple_effect', '_radius', '_ripple_rad', '_round_rad', '_text_color', '_theme_icon_color',
'_theme_text_color', 'always_release', 'anchor_x', 'anchor_y', 'center', 'center_x', 'center_y',
'children', 'cls', 'device_ios', 'disabled', 'disabled_color', 'font_name', 'font_size',
'font_style', 'halign', 'height', 'icon', 'icon_color', 'icon_size', 'id', 'ids', 'last_touch',
'line_color', 'line_color_disabled', 'line_width', 'md_bg_color', 'md_bg_color_disabled',
'min_state_time', 'motion_filter', 'opacity', 'opposite_colors', 'padding', 'parent', 'pos',
'pos_hint', 'right', 'ripple_alpha', 'ripple_canvas_after', 'ripple_color',
'ripple_duration_in_fast', 'ripple_duration_in_slow', 'ripple_duration_out',
'ripple_func_in', 'ripple_func_out', 'ripple_rad_default', 'ripple_scale', 'rounded_button',
'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y', 'size_hint_min',
'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'state', 'text', 'text_color',
'theme_cls', 'theme_icon_color', 'theme_text_color', 'top', 'valign', 'widget_style', 'width', 'x', 'y']



MAIN_DIR=os.path.dirname(sys.argv[0])+"/Files/CodeMarocAndroid"
#input(MAIN_DIR)
DIR_ANSWER=MAIN_DIR+"/Reponses"
DIR_ICONS=MAIN_DIR+"/icons"
DIR_FILE_TRUE_ANSWER_AND_NUMBER_SERIE=MAIN_DIR+"//reponse_vrais_de_serie.txt"

DIC_ANSWER={"1":"0"  ,   "2":"1",   "3":"2"  ,  "4":"3"

            ,"1-2":"5"  ,   "1-3":"6"   ,  "1-4":"7" 

            ,"2-3":"8"  ,  "2-4":"9"

            ,  "3-4":"A"

            ,  "1-2-3":"B" ,  "1-2-4":"C" ,  "1-3-4":"D" ,  "2-3-4":"E"

            ,   "1-2-3-4":"F"
            ,"-":"" , "":""}


def organizeArabicText(txt):
    reshaped_text = arabic_reshaper.reshape(txt)
    bidi_text = bidi.algorithm.get_display(reshaped_text)
    return bidi_text


def organizeAnswer(answer):
        answer_organiser=''
        answer=answer.replace(" ","")
        l=answer.split("-")
        while "" in l:
            l.remove("")
        for i in range(1,5):
            if str(i) in l:
                answer_organiser+=f"{i}-"
        answer_organiser=answer_organiser[:-1]
        if answer_organiser=="":
            answer_organiser="-"
        return answer_organiser



def load_answer(number_question):
        #read txt file
        dir_file_anwser=DIR_ANSWER+f"/{number_question}.txt"
        f=open(dir_file_anwser,"r")
        txt_answer=f.read()
        f.close()

        #
        txt_answer=organizeAnswer(txt_answer)
        print("load_answer :",txt_answer)
        return txt_answer



kv="""
<ButtonReponse@Button>:
    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
    canvas.before:
        Color:
            rgba: (0,0,1,1) if self.state=='normal' else (0,.7,.7,1)  # visual feedback of press
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [100,100,100,100]
"""

"""
<ButtonReponse@Button>:
    background_color: 0,0,0,0  # the last zero is the critical on, make invisible
    canvas.before:
        Color:
            rgba: (0,0,1,1) if self.state=='normal' else (0,.7,.7,1)  # visual feedback of press
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [250,50,]
"""

#Builder.load_string(kv)










            

    



        

   





















class LayoutPrincipalTreeButton(GridLayout):
    def __init__(self):
        super(LayoutPrincipalTreeButton,self).__init__()

        self.cols=3
        self.rows=1
        self.orientation='lr-bt'#'vertical'

        self.spacing=20
        self.height=0.2
        self.size_hint=(0.5,0.5)
        #self.button_next)

        self.w_b_n=0.1
        self.h_b_n=0.1

        self.button_qr_code=Button(text="Scan Qr")
        self.button_qr_code.font_name="arial"
        self.button_qr_code.font_size=19
        
        
        #button_answer
        self.button_four_answer=Button(text=organizeArabicText("إبدأ"))
        self.button_four_answer.font_name=self.button_qr_code.font_name
        self.button_four_answer.font_size=self.button_qr_code.font_size
        
        #self.button_four_answer.size=(50,50)
        #self.button_four_answer.size_hint=(0.1,0.2)

        
        #button_correction
        self.button_correction=Button(text=organizeArabicText("التصحيح"))
        self.button_correction.font_name=self.button_qr_code.font_name
        self.button_correction.font_size=self.button_qr_code.font_size
        #self.button_correction.size=(50,50)

        self.add_widget(self.button_qr_code)
        self.add_widget(self.button_four_answer)
        self.add_widget(self.button_correction)




       










        







class LayoutQrCode(GridLayout):
    def __init__(self,my_parent):
        super(LayoutQrCode,self).__init__()

        #
        self.my_parent=my_parent
        #attr

        self.rows=3
        self.orientation='lr-bt'#'vertical'
        
        self.h=0.2
        self.w=1
        self.i_read_qr_code=0
        self.text_read_from_qr_code=""


        #capture
        self.capture=None
        

        

        #
        self.image_qr_code=Image()
        self.image_qr_code.size_hint=(1,1)
        self.image_qr_code.text="labelCamera"
        #self.image_qr_code.background_color=(255,0,255,0)
        


        #button_open_camera
        self.button_open_camera=Button()
        self.button_open_camera.size_hint=(self.w, self.h)
        self.button_open_camera.on_press=self.openCamera
        self.button_open_camera.font_name="arial"
        self.button_open_camera.font_size=25
        self.button_open_camera.text=organizeArabicText("افتح الكاميرا")# "open Camera"
        




        self.add_widget(self.button_open_camera) 
        self.add_widget(self.image_qr_code)
        #self.add_widget(self.label_number_serie)

    def openCamera(self):
        #self.button_open_camera.text=organizeArabicText("إنتظر...")
        
        print("open camera")
        self.i_read_qr_code=0
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/33.0)



        
        
        
        

 
    def update(self, dt):
        if self.capture!=None :
            if self.i_read_qr_code==0 :
                # display image from cam in opencv window
                ret, frame = self.capture.read()
                #cv2.imshow("CV2 Image", frame)
                # convert it to texture
                buf1 = cv2.flip(frame, 0)
                try :
                    buf = buf1.tostring()
                    texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
                    #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
                    texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                    # display image from the texture
                    self.image_qr_code.texture = texture1

                    test=self.readQrCodeFromCvImage(frame)
                    if test:
                        winsound.Beep(2400,450)
                        self.i_read_qr_code=1
                        self.capture.release()
                        #cv2.destroyAllWindows()
                except :
                    pass
                

                
    def readQrCodeFromCvImage(self,frame):
        test=0
        try :
          im_pil = PIL.Image.fromarray(frame)
          decocdeQR = pyzbar.pyzbar.decode(im_pil)
          self.text_read_from_qr_code=decocdeQR[0].data.decode("ascii")
          test=1

          
          
          self.my_parent.getQrCodeData(self.text_read_from_qr_code)

          #write text on DIR_FILE_TRUE_ANSWER_AND_NUMBER_SERIE
          f=open(DIR_FILE_TRUE_ANSWER_AND_NUMBER_SERIE,"w")
          f.write(self.text_read_from_qr_code)
          f.close()


        except :
          pass 
        return test


    def stopCamera(self):
        if self.capture!=None  :
            self.capture.release()
            #cv2.destroyAllWindows()

    
        
            

    








class ButtonNumberQuestion(Button):
    def __init__(self,my_parent):
        super(ButtonNumberQuestion,self).__init__()

        self.my_parent=my_parent
        
        self.dropdown = DropDown()
        # create a dropdown with 10 buttons
        for k in range(40):
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.
            self.question_in_arabic=organizeArabicText("السؤال") 
            btn = Button(text=str(k+1)+"-"+self.question_in_arabic, size_hint_y=None, height=44)
            btn.font_name="arial"
            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: self.dropdown.select(organizeArabicText(btn.text)))

            # then add the button inside the dropdown
            self.dropdown.add_widget(btn)

        # create a big main button
        self.font_name="arial"
        self.font_size=30
        self.text=organizeArabicText("السؤال-1")#self.question_in_arabic

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        self.bind(on_release=self.dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        #self.dropdown.bind(on_select=lambda instance, x: setattr(self, 'text', organizeArabicText(x)))
        self.dropdown.bind(on_select=self.on_select )


    def on_select(self,instance,x):
        setattr(self, "text", organizeArabicText(x))
        n=int(x.split("-")[1])
        self.my_parent.go_to_specific_question(n)
        
        




class ButtonReponse(Button):
    def __init__(self,my_parent,number,size_hint):
         super(ButtonReponse,self).__init__()
         self.attribute="hello world"
         self.my_parent=my_parent
         self.number=number
         self.label_answer=self.my_parent.label_answer

         self.text=self.number

         self.my_state=0
         self.size_hint=size_hint
         self.background_color=(0,0,255,255)
         #self.color="#ffffff"
         self.font_name="arial"
         self.font_size=30
         self.line_color="green"
         self.line_width=50
         #self._radius=[50,]
         #self.rounded_button=1
         #self.border_radius=[0,25.0,25.0,25.0]
         bb=33
         #self.border = (bb,bb,bb,bb)
         #self.opacity=.3
         
         #rectangle: self.x, self.y, self.width, self.height
         #self.border=[30,30,30,30]
         #self.border = (10,10,10,10)
         #self.line_width=15

         

    def build(self,a):
        self.text="sdsdfsdfsfdsdf"


    def on_press(self):
        #print("cacllback")
        #print(self.text)
        self.my_state=1-self.my_state

        if self.my_state:
            color=(255,0,0,255)
            
        else :
            color=(0,0,255,255)     
        #print(self.my_state)
        self.background_color=color#"red"#"#ff00ff"#(1.0, 0.0, 0.0,1.0)#color#
        #self.border_radius=(200, 10, 10, 10)
        #print(self.number)
        #label_answer  text_answer
        if self.my_state :
            old_text=self.label_answer.text
            new_text=old_text+"-"+self.number
            new_answer=self.organizeAnswer(new_text)
            self.label_answer.text=new_answer
            print(new_answer)
        else :
            old_text=self.label_answer.text
            new_text=old_text.replace(self.number,"")
            new_answer=self.organizeAnswer(new_text)
            self.label_answer.text=new_answer
            print(new_answer)
        
        self.my_parent.write_answer_on_txt_file()

        print(DIC_ANSWER[new_answer])
            
    def organizeAnswer(self,answer):
        new_answer=organizeAnswer(answer)
        if new_answer=="":
            new_answer="-"
        return new_answer


    def active_me(self):
        self.my_state=1
        color=(255,0,0,255)     
        #print(self.my_state)
        self.background_color=color

    def inactive_me(self):
        self.my_state=0
        color=(0,0,255,255)     
        #print(self.my_state)
        self.background_color=color
        
        
        

    








class LayoutFourReponse(GridLayout):
    def __init__(self):
        super(LayoutFourReponse,self).__init__()

        self.number_current_question=1

        self.cols=1
        self.rows=7
        self.orientation='lr-tb'
        self.spacing=15



        #ButtonNumberQuestion
        self.ButtonNumberQuestion=ButtonNumberQuestion(self)

        #next_question
        self.next_question=Button()
        self.next_question.on_press=self.next_quetion_command
        self.next_question.font_name="arial"
        self.next_question.font_size=30
        self.next_question.text=">"#organizeArabicText("السؤال التالي")
        



        
        self.back_question=Button()
        self.back_question.text="<"#organizeArabicText("السؤال السابق")
        self.back_question.on_press=self.back_quetion_command
        self.back_question.font_name=self.next_question.font_name
        self.back_question.font_size=self.next_question.font_size
        
        #box_layout_next_back
        self.box_layout_next_back=BoxLayout()
        self.box_layout_next_back.spacing=20
        self.box_layout_next_back.size_hint=(1,1)
        self.box_layout_next_back.add_widget(self.back_question)
        self.box_layout_next_back.add_widget(self.next_question)
        



        
        #label_answer
        self.label_answer=Label(text="-")
        
        

        #ButtonReponse_1 
        self.w_b_a=1
        self.h_b_a=1.5
        self.ButtonReponse_1=ButtonReponse(self,"1",size_hint=(self.w_b_a, self.h_b_a))
        self.ButtonReponse_2=ButtonReponse(self,"2",size_hint=(self.w_b_a, self.h_b_a))
        self.ButtonReponse_3=ButtonReponse(self,"3",size_hint=(self.w_b_a, self.h_b_a))
        self.ButtonReponse_4=ButtonReponse(self,"4",size_hint=(self.w_b_a, self.h_b_a))

        #ListButtonReponse
        self.ListButtonReponse=[self.ButtonReponse_1,self.ButtonReponse_2,
                                self.ButtonReponse_3,self.ButtonReponse_4]





        
        #box_four_answer
        #self.box_four_answer=BoxLayout(spacing=40)
        #self.box_four_answer.orientation='vertical' 
        self.add_widget(self.ButtonNumberQuestion)
        self.add_widget(self.label_answer)
        self.add_widget(self.ButtonReponse_1)
        self.add_widget(self.ButtonReponse_2)
        self.add_widget(self.ButtonReponse_3)
        self.add_widget(self.ButtonReponse_4)
        self.add_widget(self.box_layout_next_back)

        #add_wiidget
        #self.add_widget(self.box_four_answer)


    
        
        
    def next_quetion_command(self):
        #get current number questiuon
        txt=self.ButtonNumberQuestion.text
        n=int(txt.split("-")[0])

        #ajouter if 1 si n<40
        if n<40  :
            n+=1

        #go_to_specific_question
        self.go_to_specific_question(n)


        #load_answer_global
        self.go_to_specific_question(n)

        

        
        



    def back_quetion_command(self):
        #get current number questiuon
        txt=self.ButtonNumberQuestion.text
        n=int(txt.split("-")[0])

        #retrancher 1 si n>11
        if n>1  :
            n-=1

        #go_to_specific_question
        self.go_to_specific_question(n)


    def go_to_specific_question(self,n):

        self.number_current_question=int(n)
        #update text ButtonNumberQuestion 
        new_text=str(n)+"-"+organizeArabicText("السؤال")
        self.ButtonNumberQuestion.text=new_text
            
        #load_answer
        txt_answer=load_answer(n)

        #acive buttons
        self.activeSpecifiqueQuestions(txt_answer)

        #
        self.label_answer.text=txt_answer

    def activeSpecifiqueQuestions(self,txt_answer):
        for i in range(1,5):
            button_reponse=self.ListButtonReponse[i-1]
            if str(i) in txt_answer :
                button_reponse.active_me()
            else :
                button_reponse.inactive_me()

    
        
  
                
        
        



    def write_answer_on_txt_file(self):
        #printing test
        print("write_answer_on_txt_file")
        #get number question
        txt=self.ButtonNumberQuestion.text
        n=int(txt.split("-")[0])
        number_question=n
        print("number_question :" , number_question)
        

        #txt_answer
        txt_answer=self.label_answer.text
        #txt_answer_convcerted_to_16=DIC_ANSWER[txt_answer]

        print("txt_answer :" ,txt_answer)

        #write_answer_on_txt_file
        dir_file_anwser=DIR_ANSWER+f"/{number_question}.txt"
        f=open(dir_file_anwser,"w")
        f.write(txt_answer)
        f.close()


    


        
        












        


class LayoutCorrection(GridLayout):
    def __init__(self):
        super(LayoutCorrection,self).__init__()

        self.rows=2
        self.cols=1
        self.orientation='lr-tb'#'vertical'
        self.height=700

        #label_result_0
        self.label_result_0=Label(text=organizeArabicText("النتيجة"))
        self.label_result_0.font_name="arial"
        self.label_result_0.font_size=19

        #label_result
        self.label_result=Label(text="36")
        self.label_result.font_name=self.label_result_0.font_name
        self.label_result.font_size=self.label_result_0.font_size

        
        #box_result
        self.box_result=BoxLayout()
        self.box_result.size_hint=(0.01,0.1)
        self.box_result.orientation='horizontal'
        self.box_result.add_widget(self.label_result)
        self.box_result.add_widget(self.label_result_0)

        
        

        #list_buttons
        self.list_buttons=[]
        
        self.layout_40_buttons=GridLayout()
        self.layout_40_buttons.size_hint=(0.9,0.9)
        self.layout_40_buttons.rows=8
        self.layout_40_buttons.cols=5
        self.layout_40_buttons.orientation='lr-tb'
        
        for i in range(40):
            b=Button()
            b.text=str(i+1)+"\n-"
            b.markup=True
            b.size_hint=(25,2)
            b.halign='center'
            b.font_size=15
            self.list_buttons.append(b)
            self.layout_40_buttons.add_widget(b)


        #add_widget
        self.add_widget(self.box_result)
        self.add_widget(self.layout_40_buttons)
            

        


        #layout_tree_bttons
        """
        self.layout_tree_bttons=GridLayout()
        self.layout_tree_bttons=GridLayout()
        self.layout_tree_bttons.cols=3
        self.layout_tree_bttons.orientation='lr-tb'
        for i in range(2):
            b=Button(text="AAAAAAA"+str(i+1))
            self.list_buttons.append(b)
            self.layout_tree_bttons.add_widget(b)"""
        

        #
        #self.add_widget(self.layout_40_buttons)
        #self.add_widget(self.layout_tree_bttons)


    def colorButtons(self):
        color_true=(0,255,0,0.7)
        color_false=(255,0,0,0.8)
        color_selected=(0,0,255,255)
        color_black=(255,255,0,0.5)

        #get_all_true_answer
        all_true_answer=self.get_all_true_answer()
        if all_true_answer!=None :
            reslut=0
            #start color
            for i in  range(len(self.list_buttons)) :
                #read anwser
                dir_file_anwser=DIR_ANSWER+f"/{i+1}.txt"
                answer=""
                if os.path.isfile(dir_file_anwser):
                    f=open(dir_file_anwser,"r")
                    answer=organizeAnswer(f.read())
                    f.close()

                #convert answer uising DIC_ANSWER
                answer_converted_using_dic_answer=""
                if  answer  in DIC_ANSWER:
                    answer_converted_using_dic_answer=DIC_ANSWER[answer]
                
                #true answer
                true_answer=all_true_answer[i:i+1]

                #CHECK IF ANSWER CORRECTION OR NOT
                if answer_converted_using_dic_answer==true_answer :
                    color=color_true
                    reslut+=1
                else :
                    color=color_false
                
                    
                
                #colro button and set text  : number and answer 
                b=self.list_buttons[i]
                b.background_color=color
                b.text=f"{i+1}\n{answer}"

                self.label_result.text=str(reslut)
            
           
        

    def get_all_true_answer(self):
        try :
            f=open(DIR_FILE_TRUE_ANSWER_AND_NUMBER_SERIE,"r")
            all_true_answer=f.read().split("-")[1]
            f.close()

            return all_true_answer
        except :
            return None
                

        



















        










class CodeMarocAndroid(App):

    def __init__(self):
        super().__init__()
        self.im_in="qr" #"qr" "4_answer" "correction"


    
        
        #icon
        self.icon = DIR_ICONS+'//icon.jpg'
        

        #button_restart
        self.unicode_up=u"\u2191"
        #self.unicode_up=u"\u27F3"
        self.unicode_down=u"\u2193"
        unicode__=u'\u2b0a'#u"\u203D"  #u'\u2b0a'   #↻
        self.button_restart=Button(text=organizeArabicText("البدء من جديد")) #text=unicode__ )#
        #self.button_restart.size_hint=(0.2,1)
        self.button_restart.font_name="arial"
        self.button_restart.font_size=19
        self.button_restart.on_press=self.restart
        #self.button_restart.background_normal=DIR_ICONS+'//reload2.png'#r"E:/PYTHON SCRIPTS/PYTHON SCRIPTS/kivy_test/qr.png"

        #button_fullscreen    
        self.button_fullscreen=Button(text=self.unicode_up)#organizeArabicText("تكبير الشاشة"))
        self.button_fullscreen.size_hint=(0.35,1)
        self.button_fullscreen.font_name="arial"
        self.button_fullscreen.font_size=19
        self.button_fullscreen.on_release=self.fullscreen_command
        self.var_fullscreen=0
        
        
        

        #label_number_serie    
        self.number_serie=0
        self.label_number_serie=Label(text=organizeArabicText("السلسلة"))
        self.label_number_serie.font_name="arial"
        self.label_number_serie.font_size=24
        

        #
        self.top_box=BoxLayout()
        #self.top_box.orientation="rl-tb"
        self.top_box.size_hint=(0.5,0.5)
        self.top_box.spacing=15
        self.top_box.add_widget(self.button_fullscreen)
        self.top_box.add_widget(self.label_number_serie)
        self.top_box.add_widget(self.button_restart)
        
        
        
        
      
        



        


        

        #LayoutFourReponse
        self.LayoutFourReponse=LayoutFourReponse()

        #LayoutQrCode
        self.LayoutQrCode=LayoutQrCode(self)

        #LayoutCorrection
        self.LayoutCorrection=LayoutCorrection()

        #center_layout
        self.center_layout=BoxLayout()
        self.center_layout.size_hint=(1,5)
        self.center_layout.add_widget(self.LayoutQrCode)
        
        


        #LayoutPrincipalTreeButton
        self.LayoutPrincipalTreeButton=LayoutPrincipalTreeButton()
        self.LayoutPrincipalTreeButton.button_qr_code.on_press=self.goToQrCode
        self.LayoutPrincipalTreeButton.button_four_answer.on_press=self.goToFourAnswer
        self.LayoutPrincipalTreeButton.button_correction.on_press=self.goToCorrection
        
        

        self.main_layout=GridLayout(spacing=20)
        self.main_layout.orientation="lr-tb"
        self.main_layout.rows=3
        self.main_layout.cols=1
        
        self.main_layout.add_widget(self.top_box )
        self.main_layout.add_widget(self.center_layout)
        self.main_layout.add_widget(self.LayoutPrincipalTreeButton)

        #call start
        self.start()
        self.goToFourAnswer()
        
        
        

    def build(self):
        return self.main_layout


    def fullscreen_command(self):
        self.var_fullscreen=1-self.var_fullscreen
        if self.var_fullscreen:
            self.main_layout.remove_widget(self.LayoutPrincipalTreeButton)

            #remove_widget from top_box
            self.top_box.remove_widget(self.button_restart)
            self.top_box.remove_widget(self.label_number_serie)

            #button_fullscreen updtate fleche
            self.button_fullscreen.text=self.unicode_down

            #Window.fullscreen
            Window.fullscreen = True
            

            """
            self.top_box.add_widget(self.button_restart)
            self.top_box.add_widget(self.label_number_serie)
            self.top_box.add_widget(self.button_fullscreen)
            """
        else :
            self.main_layout.add_widget(self.LayoutPrincipalTreeButton)

            #add_widget to  top_box
            self.top_box.add_widget(self.label_number_serie)
            self.top_box.add_widget(self.button_restart)

            #button_fullscreen updtate fleche
            self.button_fullscreen.text=self.unicode_up

            #Window.fullscreen
            Window.fullscreen = False

              
            

            
    
    def goToQrCode(self):
        if self.im_in!="qr" : #"qr" "4_answer" "correction"
            print("goToQrCode")
            self.center_layout.add_widget(self.LayoutQrCode)
            self.center_layout.remove_widget(self.LayoutFourReponse)
            self.center_layout.remove_widget(self.LayoutCorrection)
            self.im_in="qr"

    def goToFourAnswer(self):
        if self.im_in!="4_answer" : #"qr" "4_answer" "correction" self.LayoutFourReponse
            print("goToFourAnswer")
            self.center_layout.remove_widget(self.LayoutQrCode)
            self.center_layout.add_widget(self.LayoutFourReponse)
            self.center_layout.remove_widget(self.LayoutCorrection)
            self.im_in="4_answer"
            self.stopCamera()

            #load self.number_current_question
            n=self.LayoutFourReponse.number_current_question
            self.LayoutFourReponse.go_to_specific_question(n)
            

    def goToCorrection(self):
        if self.im_in!="correction" : #"qr" "4_answer" "correction"
            print("goTo40Answer")
            self.center_layout.remove_widget(self.LayoutQrCode)
            self.center_layout.remove_widget(self.LayoutFourReponse)
            self.center_layout.add_widget(self.LayoutCorrection)
            
            #stop camera
            self.im_in="correction"
            self.stopCamera()

            #colorButtons
            self.LayoutCorrection.colorButtons()
            
            
            

    def stopCamera(self):
        if self.im_in!="qr" : 
            self.LayoutQrCode.stopCamera()

    def getQrCodeData(self,text_read_from_qr_code):
        print("getQrCodeData")
        print(text_read_from_qr_code)

        #update number serie
        self.number_serie=int(text_read_from_qr_code.split("-")[0])

        #update label
        reshaped_text = arabic_reshaper.reshape("السلسلة")
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        self.label_number_serie.text=str(self.number_serie)+" : "+str(bidi_text)


    def create_folder_and_files(self):
        #hadi bach t creer les dossiers w l fichiers fach yallah t installa l'application
        #main_dir
        os.makedirs(MAIN_DIR, exist_ok=1)

        #DIR_ANSWER
        os.makedirs(DIR_ANSWER, exist_ok=1)

        #creat_file_true_answer
        if  not os.path.isfile(DIR_FILE_TRUE_ANSWER_AND_NUMBER_SERIE):
                #create file if not exist
                f=open(DIR_FILE_TRUE_ANSWER_AND_NUMBER_SERIE,"w")
                f.close()
                
        

        #creta_txt_file_answer
        for i in range(40):
            dir_file_anwser=DIR_ANSWER+f"/{i+1}.txt"
            if  not os.path.isfile(dir_file_anwser):
                #create file if not exist
                f=open(dir_file_anwser,"w")
                f.close()

    def restart(self):
         
        self.popuplayout = GridLayout(cols = 1, padding = 10)
 
        self.popupLabel = Label(text = organizeArabicText('هل تريد البدء من جديد ؟'))
        self.popupLabel.font_size=19
        

        self.popupLabel.font_name="arial"
        self.yesButton = Button(text =  organizeArabicText('نعم'))
        self.yesButton.font_size=self.popupLabel.font_size
        self.yesButton.font_name=self.popupLabel.font_name
        
        self.noButton = Button(text = organizeArabicText(' لا'))
        self.noButton.font_size=self.popupLabel.font_size
        self.noButton.font_name=self.popupLabel.font_name
        
        self.closeButton = Button(text = organizeArabicText("إغلاق"))
        self.closeButton.font_size=self.popupLabel.font_size
        self.closeButton.font_name=self.popupLabel.font_name

        #box_layout_buttons
        self.popup_box_layout_buttons=BoxLayout()
        self.popup_box_layout_buttons.orientation="horizontal"
        self.popup_box_layout_buttons.add_widget(self.closeButton)
        self.popup_box_layout_buttons.add_widget(self.noButton)
        self.popup_box_layout_buttons.add_widget(self.yesButton)
        
        
 
        self.popuplayout.add_widget(self.popupLabel)
        self.popuplayout.add_widget(self.popup_box_layout_buttons)       
 
        # Instantiate the modal popup and display
        self.popup = Popup(title ="CodeMarocAndroid",
                      content = self.popuplayout,
                      size_hint =(None, None), size =(300, 200))
        
        self.popup.open()   
 
        # Attach close button press with popup.dismiss action
        self.closeButton.bind(on_press = self.popup.dismiss)
        self.noButton.bind(on_press = self.popup.dismiss)
        self.yesButton.bind(on_press =self.vider_files_answer )

    def vider_files_answer(self,event):
        #write nothing in txt files
        for i in range(40):
            dir_file_anwser=DIR_ANSWER+f"/{i+1}.txt"
            f=open(dir_file_anwser,"w")
            f.close()

        #go to fisrt question
        self.LayoutFourReponse.go_to_specific_question(1)

        #
        self.popup.dismiss()


    def start(self):
        print("start")
        #create folder and file if not exist
        self.create_folder_and_files()

        #load number serie

        f=open(DIR_FILE_TRUE_ANSWER_AND_NUMBER_SERIE,"r")
        self.number_serie=f.read().split("-")[0]
        f.close()

        #write on labe       
        txt= str(self.number_serie)+" "+organizeArabicText("السلسلة ")
        self.label_number_serie.text=txt
        
        
        
                    

       
        
        
        




        
#runTouchApp(ButtonReponse(text="Hit Me!"))
if __name__ == '__main__':
    C=CodeMarocAndroid()
    C.start()
    C.run()
    
