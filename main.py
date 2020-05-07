from tkinter import * #tkinter =)
from tkinter.font import Font #import module to customize font
from PIL import ImageTk, Image #import modules to import image
from PyDictionary import PyDictionary #import the dictionary
import requests #import this to request the webpage
from bs4 import BeautifulSoup #to get data from the requested webpage

global dic #globalize the dictionary data
dic = PyDictionary() #get the dictionary data

def init(): #initialize the app

    #setup window
    global root #globalize the root
    root = Tk() #create main window
    root.config(bg='white') #set the bg color to a nice grey color
    root.title('Python Dictionary GUI') #give the window a title
    root.geometry('500x350') #resize the window
    root.iconbitmap('icon.ico') #give the window a nice icon
    root.resizable(False, False) #make the window unresizable

    #setup font
    global titlefont #globalize the title font style
    global inputfont #globalize the input font style
    global buttonfont #globalize the button font style
    global nafont #globalize the 'not available' label font
    global meaningfont #globalize the meaning box font
    global tabfont #globalize the font for the tab menu bar
    titlefont = Font(size=30, family='Bahnschrift') #setup title style
    nafont = Font(size=20, family='Bahnschrift Light') #set the font style of the 'not available' font style'
    inputfont = Font(size=20, family='Corbel') #setup inputbox font sytle
    buttonfont = Font(size=15, family='Franklin Gothic Medium') #set the button text font style
    tabfont = Font(size=15, family='Bahnschrift Light') #set the tab menu text font style
    meaningfont = Font(size=15) #setup the meaning box font style

    #setup icon
    global mainicon #globalize the icon
    mainicon = ImageTk.PhotoImage(Image.open("icon.png")) #load the icon

def menu(): #menu
    init() #initialize the app first

    global na_message #globalize the 'not available message'
    global search_input #globalize the search input box

    def search(): #search for the word
        global search_input #globalize teh search input box again
        global tabbtnframe #globalize the meaning textbox frame
        global textbox #globalize the meaning textbox
        global meaningtabbtn #globalize the meaning tab button
        global syntabbtn #globalize the synonym tab button
        global anttabbtn #globalize the antonym tab button
        global na_message #globalize the 'not available' message label
        global synonym #globalize the synonym list
        global antonym #globalize the antonym list
        word = search_input.get() #get the data from the search box
        synonym = [] #create a list for the synonym
        antonym = [] #create the list for the antonym
        meaning = dic.meaning(word) #search for the word in the dictionary

        URL = 'https://www.synonym.com/synonyms/'+word #generate the url by putting the word in
        page = requests.get(URL) #request the url

        soup = BeautifulSoup(page.content, 'html.parser') #get the html from requested webpage
        try: #try it
            syn = soup.find('div', {'class':'card full-width mdc-card type-synonym'}).find('div', {'class':'card-content'}).findAll('a') #find the data we want
            for i in syn: #form a loop
                synonym.append(i.text) #append every text from the gotten data into the list
            for i in range(len(synonym)): #from another loop
                synonym[i] = ''.join(synonym[i].replace('\n','').split()) #clear the rubbish
        except: #if cannot find the synonym
            synonym=['NONE'] #nothing
        try: #try it
            ant = soup.find('div', {'class':'card full-width mdc-card type-antonym'}).find('div', {'class':'card-content'}).findAll('a') #get the data from the webpage
            for i in ant: #form a loop
                antonym.append(i.text) #append every text from the gotten data into the list
            for i in range(len(antonym)): #form another loop
                antonym[i] = ''.join(antonym[i].replace('\n','').split()) #get rid of the rubbish
        except: #if cannot find the data
            antonym=['NONE'] #nothing
        
        if meaning == None: #if the word is not available
            print('not available') #print out 'not abailable' in the console
            
            na_message = Label( #make a label in the window
                root, #in the root window
                text='word not available', #the label content
                font=nafont, #set the font style
                bg='white', #set the background color
                fg='#FF7D7D' #set the word color
                )
            
            na_message.place(x=135,y=290) #place the label
            try: #try if it is possible
                tabbtnframe.place_forget()  #forget the meaningbox frame
                textbox.place_forget() #forget the word meaning box
                meaningtabbtn.place_forget() #forget the tab button
                syntabbtn.place_forget() #forgte the tab button
                anttabbtn.place_forget() #forget the tab button
                root.geometry('500x350') #resize the window back to normal
                
            except: #if not possible
                pass #do nothing
            
        else: #if the word exist
            global key #globalize the key of the meaning
            global values #globalize the value of the meaning
            try: #try it
                syntabbtn.place_forget() #forget the tab button
                meaningtabbtn.place_forget() #forget the tab button
                anttabbtn.place_forget() #forget the antonym button
            except: #if cannot
                pass #pass it
            
            root.geometry('500x750') #make the window bigger to show the meaning box
            try: #try it
                na_message.place_forget() #forget the 'not available' message label
            except: #if cannot
                pass #just pass it

            def meaningtabbtn_on_enter(e): #button detection
                if meaningtabbtn['state']==NORMAL:
                    meaningtabbtn['background'] = '#1A73E8'
                    meaningtabbtn['fg'] = 'white'
            def meaningtabbtn_on_leave(e): #button detection
                if meaningtabbtn['state']==NORMAL:
                    meaningtabbtn['background'] = '#F1F1F3'
                    meaningtabbtn['fg'] = '#656567'
            def syntabbtn_on_enter(e): #button detection
                if syntabbtn['state']==NORMAL:
                    syntabbtn['background'] = '#1A73E8'
                    syntabbtn['fg'] = 'white'
            def syntabbtn_on_leave(e): #button detection
                if syntabbtn['state']==NORMAL:
                    syntabbtn['background'] = '#F1F1F3'
                    syntabbtn['fg'] = '#656567'
            def anttabbtn_on_enter(e): #button detection
                if anttabbtn['state']==NORMAL:
                    anttabbtn['background'] = '#1A73E8'
                    anttabbtn['fg'] = 'white'
            def anttabbtn_on_leave(e): #button detection
                if anttabbtn['state']==NORMAL:
                    anttabbtn['background'] = '#F1F1F3'
                    anttabbtn['fg'] = '#656567'

            tabbtnframe = Frame( #the frame of the meaning box
                root, #in the root
                width=454, #the width of the frame
                height=351, #the height of the frame
                bg='#1A73E8' #set the colof of the frame
                )

            def synonymfunc(): #what to do when the synonym tab button pressed
                global meaningtabbtn #globalize the meaning tab button
                global anttabbtn #globalize the antonym tab button
                global syntabbtn #globalize the synonym tab button
                global textbox #globalize the text container
                meaningtabbtn.place_forget() #forget the meaning tab button
                anttabbtn.place_forget() #forget the antonym tab button
                syntabbtn.place_forget() #forget the synonym tab button 
                meaningtabbtn.config(bg='#F1F1F3', fg='#656567', state=NORMAL, pady=1) #config the meaning tabbutton
                anttabbtn.config(bg='#F1F1F3', fg='#656567', state=NORMAL, pady=1) #config the antonym tab button
                syntabbtn.config(bg='#1A73E8', fg='white', state=DISABLED, pady=3) #config the synonym tab button so that it is unpressable
                meaningtabbtn.place(x=24, y=310) #replace the meaning tab button
                syntabbtn.place(x=174, y=310) #replace the synonym tab button
                anttabbtn.place(x=325, y=310) #replace the antonymtab button
                meaningtabbtn.bind("<Enter>", meaningtabbtn_on_enter) #detect if the button is being hovered by mouse
                meaningtabbtn.bind("<Leave>", meaningtabbtn_on_leave) #detect if the mouse left the button
                syntabbtn.bind("<Enter>", syntabbtn_on_enter) #detect if the button is being hovered by mouse
                syntabbtn.bind("<Leave>", syntabbtn_on_leave) #detect if the mouse left the button
                anttabbtn.bind("<Enter>", anttabbtn_on_enter) #detect if the button is being hovered by mouse
                anttabbtn.bind("<Leave>", anttabbtn_on_leave) #detect if the mouse left the button

                textbox.place_forget() #forget the textbox
                textbox.config(state=NORMAL) #set the textbox back to normal
                textbox.delete(0.0,END) #delete all content of the textbox
                textbox.place(x=24, y=357) #replace the textbox

                for i in synonym: #loop inside the meaning list
                    textbox.insert(END,('\u21D2  '+i+'\n')) #dump the meaning into the textbox one by one

                textbox.config(state=DISABLED) #reconfig the textbox so that it is untouchable

            def meaningfunc(): #what to do when the meaning tab button pressed
                global meaningtabbtn #globalize the meaning tab button
                global anttabbtn #globalize the antonym tab button
                global syntabbtn #globalize the synonym tab button
                global textbox #globalize the text container
                global key #globalize the key of the word meaning
                global values #globalize the value of the word meaning
                meaningtabbtn.place_forget() #forget the meaning tab button
                anttabbtn.place_forget() #forget the antonym tab button
                syntabbtn.place_forget() #forget teh synonym tab button
                meaningtabbtn.config(bg='#1A73E8', fg='white', state=DISABLED, pady=3) #config the meaning tab button so it cannot get press
                anttabbtn.config(bg='#F1F1F3', fg='#656567', state=NORMAL, pady=1) #config the antonym button
                syntabbtn.config(bg='#F1F1F3', fg='#656567', state=NORMAL, pady=1) #config the synonym button
                meaningtabbtn.place(x=24, y=310) #replace the meaning buton
                syntabbtn.place(x=174, y=310) #config the synonym button
                anttabbtn.place(x=325, y=310) #config the antonym button
                meaningtabbtn.bind("<Enter>", meaningtabbtn_on_enter) #detect if the button is being hovered by mouse
                meaningtabbtn.bind("<Leave>", meaningtabbtn_on_leave) #detect if the mouse left the button
                syntabbtn.bind("<Enter>", syntabbtn_on_enter) #detect if the button is being hovered by mouse
                syntabbtn.bind("<Leave>", syntabbtn_on_leave) #detect if the mouse left the button
                anttabbtn.bind("<Enter>", anttabbtn_on_enter) #detect if the button is being hovered by mouse
                anttabbtn.bind("<Leave>", anttabbtn_on_leave) #detect if the mouse left the button

                textbox.grid_forget() #forget teh text container
                textbox.config(state=NORMAL) #set the container back to normal
                textbox.delete(0.0,END) #delete entire content in the textbox
                textbox.place(x=24, y=357) #replace the textbox

                textbox.tag_configure('highlightline', background='white', foreground='black', font='helvetica 14 italic', relief='raised') #set the style of the meaning keys

                for i in range(len(key)): #form a loop that go through all the keys
                    textbox.insert(END,key[i]+'\n',('highlightline')) #print out the keys with previously setup font style
                    
                    for m1 in values[i]: #form a loop that go through all the values in the word meaning
                        textbox.insert(END, '\u21D2  '+m1+'\n') #insert them into the container
                    textbox.insert(END, '\n') #insert a blank line after that

                textbox.config(state=DISABLED) #lock the container
                
            def antonymfunc(): #what to do when the meaning tab button pressed
                global meaningtabbtn #globalize the meaning tab button
                global anttabbtn #globalize the antonym tab button
                global syntabbtn #globalize the synonym tab button
                global textbox #globalize the text container
                meaningtabbtn.place_forget() #forget the meaning tab button
                anttabbtn.place_forget() #forget the antonym tab button
                syntabbtn.place_forget() #forget teh synonym tab button
                meaningtabbtn.config(bg='#F1F1F3', fg='#656567', state=NORMAL, pady=1) #config the meaning tab button
                anttabbtn.config(bg='#1A73E8', fg='white', state=DISABLED, pady=3) #config the antonym tab button so that is cannot be pressed
                syntabbtn.config(bg='#F1F1F3', fg='#656567', state=NORMAL, pady=1) #config the aynonym tab button
                meaningtabbtn.place(x=24, y=310) #replace the meaning tab button
                syntabbtn.place(x=174, y=310) #replace the synonym tab button
                anttabbtn.place(x=325, y=310) #replace the antonym tab button
                meaningtabbtn.bind("<Enter>", meaningtabbtn_on_enter) #detect if the button is being hovered by mouse
                meaningtabbtn.bind("<Leave>", meaningtabbtn_on_leave) #detect if the mouse left the button
                syntabbtn.bind("<Enter>", syntabbtn_on_enter) #detect if the button is being hovered by mouse
                syntabbtn.bind("<Leave>", syntabbtn_on_leave) #detect if the mouse left the button
                anttabbtn.bind("<Enter>", anttabbtn_on_enter) #detect if the button is being hovered by mouse
                anttabbtn.bind("<Leave>", anttabbtn_on_leave) #detect if the mouse left the button

                textbox.grid_forget() #forget the text container
                textbox.config(state=NORMAL) #set the container back to normal
                textbox.delete(0.0,END) #delete all content in the list
                textbox.place(x=24, y=357) #replace the text container

                for i in antonym: #loop inside the meaning list
                    textbox.insert(END,('\u21D2  '+i+'\n')) #dump the meaning into the textbox one by one

                textbox.config(state=DISABLED) #lock the container

            meaningtabbtn = Button( #setup the meaning tab button
                root, #in the root
                text='MEANING', #set the text in the button
                bg='#1A73E8', #set the background color
                fg='white', #set the foreground color
                font=tabfont, #dump in the font style
                relief=FLAT, #no 3D
                padx=21.9, #set the pady
                pady=3, #set the padx
                disabledforeground='white', #set the background when the button is being disabled
                state=DISABLED, #disable the button
                command=meaningfunc, #set what thing to do when the button get press
                activebackground='#1A73E8', #set the background while being pressed
                activeforeground='white' #set the foreground while being pressed
                )
            syntabbtn = Button( #setup the synonym tab button
                root, #in the root
                text='SYNONYM', #set the text in the button
                bg='#F1F1F3', #set the background color
                fg='#656567', #set the foreground color
                font=tabfont, #dump the font style into the button
                relief=FLAT, #no 3D
                padx=21.9, #set the padx
                pady=1, #set the pady
                disabledforeground='white', #set the background when the button is being disabled
                command=synonymfunc, #set what thing to do when the button get press
                activebackground='#1A73E8', #set the background while being pressed
                activeforeground='white' #set the foreground while being pressed
                )
            anttabbtn = Button( #setup the antonym button
                root, #in the root
                text='ANTONYM', #set the text in the button
                bg='#F1F1F3', #set the background of the button
                fg='#656567', #set the foreground of the button
                font=tabfont, #set the font style of the button
                relief=FLAT, #no 3D
                padx=22, #set the padx
                pady=1, #set the pady
                disabledforeground='white', #set the background when disabled
                command=antonymfunc, #what to do when being pressed
                activebackground='#1A73E8', #set the bgcolor when being pressed
                activeforeground='white' #set teh bgcolor when being pressed
                )

            values = list(dic.meaning(word).values()) #sort out the values of the meaning
            key = list(dic.meaning(word)) #sort out the key of the meaning

            for i in range(len(values)): #form a loop
                for h in range(len(values[i])): #form a loop inside a loop
                    values[i][h] = values[i][h].replace('(','') #replace the useless thing to nothing
            
            textbox=Text( #create the textbox to dump in the meaning
                root, #in the root
                bg='white', #set the background color
                width=40, #set the width of the textbox
                height=15, #set the height of the textbox
                fg='#757575', #set the color of the text
                relief=FLAT, #no 3D
                borderwidth=0, #set the borderwidth to 0
                padx=5, #set some distance between text and frame
                font=meaningfont #set the font style
                )

            textbox.tag_configure( #set the tag style
                'highlightline', #set the name
                background='white', #set the bgcolor
                foreground='black', #set the fgcolor
                font='helvetica 14 italic', #set the font
                relief='raised' #set the relief of the font
                )

            for i in range(len(key)): #form a loop
                textbox.insert(END,key[i]+'\n',('highlightline')) #dump the key into the container
                
                for m1 in values[i]: #a loop inside a loop
                    textbox.insert(END, '\u21D2  '+m1+'\n') #insert the values into the container
                textbox.insert(END, '\n') #insert a blank line after that
                
            tabbtnframe.place(x=22, y=355) #place down the frame
            textbox.config(state=DISABLED) #set the textbox state so that user can't edit it
            textbox.place(x=24, y=357)  #place the textbox inside the root window
            meaningtabbtn.place(x=24, y=310) #place down the tab button
            syntabbtn.place(x=174, y=310) #place down the tab button
            anttabbtn.place(x=325, y=310) #place down the tab button
            meaningtabbtn.bind("<Enter>", meaningtabbtn_on_enter) #detect if the button is being hovered by mouse
            meaningtabbtn.bind("<Leave>", meaningtabbtn_on_leave) #detect if the mouse left the button
            syntabbtn.bind("<Enter>", syntabbtn_on_enter) #detect if the button is being hovered by mouse
            syntabbtn.bind("<Leave>", syntabbtn_on_leave) #detect if the mouse left the button
            anttabbtn.bind("<Enter>", anttabbtn_on_enter) #detect if the button is being hovered by mouse
            anttabbtn.bind("<Leave>", anttabbtn_on_leave) #detect if the mouse left the button


    def on_click(event): #input box detection
        search_input.configure(state=NORMAL)
        search_input.delete(0, END)
        search_input.unbind('<Button-1>', on_click_id)

    def button_on_enter(e): #button detection
        if submit_button['state']==NORMAL:
            submit_button['background'] = '#1A73E8'
            submit_button['fg'] = 'white'

    def button_on_leave(e): #button detection
        if submit_button['state']==NORMAL:
            submit_button['background'] = 'white'
            submit_button['fg'] = '#1A73E8'

    titleicon = Label( #title icon
        root, #in the root window
        bg='white', #bg color same as window
        image=mainicon #shown as the icon
        )

    title = Label(  #title label
        root, #in the root window
        text='Python Dictionary', #the title
        font=titlefont, #load the font style
        bg='white', #bg same as the window
        fg='#757575' #fg is #757575
        )

    searchframe = Frame( #search input box frame
        root, #in the root window
        width=342, #set the width
        height=64, #set the height
        background='#1A73E8', #nice green color
        borderwidth=1 #set the borderwidth 
        )
    
    search_input = Entry( #search input box
        root, #in the root window
        disabledbackground='white', #color when the search box is disabled
        font=inputfont, #set the font style
        borderwidth=0, #set the borderwidth to 0
        fg='#757575', ##757575color text
        bg='white', #bg same as the window
        relief=FLAT, #no 3D
        justify=CENTER, #let the text to be in the center
        width=24, #set the width of the input box
        insertbackground='#757575', #set the cursor color to #757575
        disabledforeground='#757575' #set the foreground to light ligth grey when disabled
        )

    submitbuttonframe = Frame( #the frame of the submit button
        root, #in the root window
        width=344, #set the frame width
        height=64, #set the frame height
        background='#1A73E8' #set he bg to a nice green color
        ) 

    submit_button = Button( #the real submit button
        root, #in the root window
        activebackground='#1A73E8', #set the bg when mouse clicked
        activeforeground='white', #set the fg when the mouse clicked
        fg='#1A73E8', #set the real fg
        text='SEARCH', #set the text of the button
        font=buttonfont, #make it look cooler
        pady=9, #make the button look taller
        width=30, #make the button look fatter
        bg='white', #set the bg of the button
        relief=FLAT, #no ugly 3D
        command=search #whent this button get clicked it will execute the search function
        )

    titleicon.place(x=60,y=23) #place the titleicon
    title.place(x=115,y=20) #place the title label
    searchframe.place(x=80,y=130) #place the frame of the search box
    search_input.place(x=82,y=132,height=60) #place the search box
    search_input.insert(0, 'type your word here') #initalize the search box and give you a hint what to do
    search_input.configure(state=DISABLED) #disabled the search box unless you click it
    submitbuttonframe.place(x=79,y=210) #place the frame of the submit button
    submit_button.place(x=81,y=212) #place the real submit button
    on_click_id = search_input.bind('<Button-1>', on_click) #detect if the search box being clicked
    submit_button.bind("<Enter>", button_on_enter) #detect if the button is being hovered by mouse
    submit_button.bind("<Leave>", button_on_leave) #detect if the mouse left the button

if __name__ == '__main__': #if this is the main application or something like that
    menu() #start the app
    root.mainloop() #start the window
