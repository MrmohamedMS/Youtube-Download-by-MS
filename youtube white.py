import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
import pyperclip

def Widgets():

################################################################################################### first head 
	head_label = Label(MS, 
					text=" BY. MOHAMED ELSAYED ",
					padx=15,
					pady=15,
					bg="#ECF2FF",
                    font="Arial 25 bold",
					fg="#3E54AC")
	head_label.grid(row=0,
					column=0,
					pady=10,
					padx=15,
					columnspan=3)
#################################################################################################### secend head 
	link_label = Label(MS,
					text="YouTube link : >>>> ",
					font="Arial 14 bold",
					bg="#ECF2FF",
					pady=5,
                    fg="#3E54AC",
					padx=5)
	link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)

	MS.linkText = Entry(MS,
						width=35,
						textvariable=video_Link,
						font="Arial 14")
	MS.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)
################################################################################################### button to paste link
	browse_A = Button(MS,
					text="Paste",
					command=update_text,
					width=7,
                    font="Arial 10 bold",
					bg="#BFACE2",
                    fg="#3E54AC",
					relief=GROOVE)
	browse_A.grid(row=2,
				column=3,
				pady=1,
				padx=1)
################################################################################################### h3 
	Downloadlocation_label = Label(MS,
							text="Download location : >>>>",
							font="Arial 14 bold",
							bg="#ECF2FF",
                            fg="#3E54AC",
							pady=5,
							padx=9)
	Downloadlocation_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


	MS.Downloadlocation_Text = Entry(MS,
								width=27,
								textvariable=download_Path,
								font="Arial 14")
	MS.Downloadlocation_Text.grid(row=3,
							column=1,
							pady=5,
							padx=5)

################################################################################################### choose file to download by button Browse and button download vedio

	browse_B = Button(MS,
					text="Browse",
                    font ="Arial 10 bold",
					command=Browse,
					width=10,
					bg="#BFACE2",
                    fg="#3E54AC",
					relief=GROOVE)
	browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)

	Download_B = Button(MS,
						text="Download Video",
						command=Download,
						width=20,
						bg="#BFACE2",
                        fg="#3E54AC",
						pady=10,
						padx=15,
						relief=GROOVE,
						font="Arial, 14 bold")
	Download_B.grid(row=4,
					column=0,
					pady=10,
					padx=10)

###############################################################################################################	button to download audio		

	Download_C = Button(MS,
						text="Download Audio",
						command=Downloader,
						width=20,
						bg="#BFACE2",
                        fg="#3E54AC",
						pady=10,
						padx=15,
						relief=GROOVE,
						font="Arial, 14 bold")
	Download_C.grid(row=5,
					column=0,
					pady=20,
					padx=20)

# to paste link from youtube

def update_text():
   global linkText 
   MS.linkText.insert(END,pyperclip.paste())

def Browse():

	download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")

	download_Path.set(download_Directory)

# to download the video

def Download():

	Youtube_link = video_Link.get()

	# saving file's
	download_Folder = download_Path.get()

	# Creating object of YouTube()
	getVideo = YouTube(Youtube_link)

	# to save high q
	videoStream = getVideo.streams.get_highest_resolution()

	videoStream.download(download_Folder)
	# Displaying the message
	messagebox.showinfo("Done",
						"Downloaded and saved in \n"
						+ download_Folder)


# to download the audio

def Downloader():


	Youtube_link = video_Link.get()

	download_Folder = download_Path.get()

	getVideo = YouTube(Youtube_link)

	videoStream = getVideo.streams.get_by_itag(251)

	videoStream.download(download_Folder)

	messagebox.showinfo("Done",
						"Downloaded and saved in \n"
						+ download_Folder)



# Creating object of tk class

MS = tk.Tk()


MS.geometry("790x380")
MS.resizable(False, False)
MS.title("MOHAMED ELSAYED")
MS.config(background="#ECF2FF")



video_Link = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()



MS.mainloop()

