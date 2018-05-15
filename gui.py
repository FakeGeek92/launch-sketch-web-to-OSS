from tkinter import *
import re
from main_func import PublishWeb
import os

class EntryFrame(Frame):
    def __init__(self, title_label, placeholder, prompt_label, master):
        Frame.__init__(self, master)
        self.title_label = title_label
        self.placeholder = placeholder
        self.prompt_label = prompt_label
        self.TitleLabel = Label(self, text=self.title_label, fg='#000000', font='SFProDisplay 16')
        self.EntryBox = Entry(self, width=40, fg='#999999', font='SFProDisplay 14')
        self.PromptLabel = Label(self, text=self.prompt_label, fg='#666666', wraplength=350, justify=LEFT,
                                 font='SFProDisplay 12')
        # self.create_entry_frame()
        self.pack()

    def create_entry_frame(self):
        self.TitleLabel.pack(anchor=W)
        self.EntryBox.insert(0, self.placeholder)
        self.EntryBox.pack(fill=X, anchor=W)
        self.PromptLabel.pack(fill=X, anchor=W, side=LEFT)


class PublishWebWindow:
    def __init__(self):
        self.url_tl = 'Anima Preview Website URL'
        self.url_ep = 'https://launchpad.animaapp.com/preview/xxxxxx'
        self.url_pl = 'The URL you got when you used the Anima-toolkit to preview website.'

        self.html_tl = 'Html Name'
        self.html_ep = 'the-product-intro'
        self.html_pl = 'The name of the html file. Use ‘-’ to connect words.'

        self.oss_img_folder_tl = 'Aliyunoss Bucket Image Folder'
        self.oss_img_folder_ep = 'imgs/the-product-intro-imgs'
        self.oss_img_folder_pl = 'If you have parent folder, add the parent folder name and "/" ' \
                                 'before the folder. Use ‘-’ to connect words.'

        self.oss_html_folder_tl = 'Aliyunoss Bucket Html Folder'
        self.oss_html_folder_ep = 'htmls'
        self.oss_html_folder_pl = ''

        # main frame
        self.main_frame = Frame()

        # url frame
        self.url_frame = Frame(self.main_frame)
        self.url_ef = EntryFrame(self.url_tl, self.url_ep, self.url_pl, self.url_frame)

        self.sep_frame1 = Frame(height=10, master=self.main_frame)

        # html name frame
        self.html_frame = Frame(self.main_frame)
        self.html_ef = EntryFrame(self.html_tl, self.html_ep, self.html_pl, self.html_frame)

        self.sep_frame2_1 = Frame(self.main_frame, height=15)
        self.c = Canvas(self.main_frame, width=450, height=1, bg="#CCCCCC")
        self.sep_frame2_2 = Frame(self.main_frame, height=15)

        # ALiyunOss img_folder frame
        self.oss_img_folder_frame = Frame(self.main_frame)
        self.oss_img_folder_ef = EntryFrame(self.oss_img_folder_tl, self.oss_img_folder_ep,
                                            self.oss_img_folder_pl, self.oss_img_folder_frame)

        self.sep_frame3 = Frame(self.main_frame, height=10)

        # ALiyunOss html_folder frame
        self.oss_html_folder_frame = Frame(self.main_frame)
        self.oss_html_folder_ef = EntryFrame(self.oss_html_folder_tl, self.oss_html_folder_ep,
                                             self.oss_html_folder_pl, self.oss_html_folder_frame)

        # Publish button
        self.pub_button = Button(self.main_frame, background='#9013FE', width=40, height=2,
                                 font='SFProDisplay 19', foreground='#FFFFFF', text='Publish',
                                 command=self.get_all_entry_value)

    def get_all_entry_value(self):
        module_path = os.path.dirname(__file__)
        print(module_path)
        os.chdir(module_path)

        set_config_value('web_url', self.url_ef.EntryBox.get())
        set_config_value('web_name', self.html_ef.EntryBox.get())
        set_config_value('imgs_oss_bucket_folder', self.oss_img_folder_ef.EntryBox.get())
        set_config_value('html_oss_bucket_folder', self.oss_html_folder_ef.EntryBox.get())
        print('Publish config update!')

        pw = PublishWeb()
        pw.generate_html_file()
        pw.upload_html_and_delete_local_temp_file()



    def draw_publish_window(self):
        self.url_ef.create_entry_frame()
        self.url_frame.pack(anchor=W)

        self.sep_frame1.pack()

        self.html_ef.create_entry_frame()
        self.html_frame.pack(anchor=W)

        self.sep_frame2_1.pack()
        self.c.pack()
        self.sep_frame2_2.pack()

        self.oss_img_folder_ef.create_entry_frame()
        self.oss_img_folder_frame.pack(anchor=W)

        self.sep_frame3.pack()

        self.oss_html_folder_ef.create_entry_frame()
        self.oss_html_folder_frame.pack(anchor=W)

        self.pub_button.pack()

        self.main_frame.pack(padx=100, pady=30)


def draw_window():
    window = Tk()
    window.title('Publish website from LaunchPad')
    window.geometry("550x500")
    window.resizable(0, 0)

    # menubar = Menu(title='fuck')
    # menubar.add_command(lable='preference', command=set_preference)
    # menubar.add_command(lable='Quit', command=window.quit)

    pb = PublishWebWindow()
    pb.draw_publish_window()

    # draw_input_frame()
    # draw_menu(window)

    window.mainloop()


def set_config_value(config_item, value):
    rep_line = config_item + ' = ' + '\'' + value + '\''
    pattern = re.compile(r'' + config_item + '.*\'')

    f = open('config.py', 'r')
    temp_file = ''

    for line in f:
        if config_item in line:
            line = re.sub(pattern, rep_line, line)
            print('repled_line:' + line)
            temp_file += line
        else:
            temp_file += line
    f.close()
    # print(temp_file)
    w = open('config.py', 'w')
    w.write(temp_file)
    w.close()


if __name__ == '__main__':
    # test()
    # main()
    draw_window()