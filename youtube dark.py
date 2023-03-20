import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
import pyperclip
def Widgets():


	head_label = Label(root, 
					text=" BY . MOHAMED ELSAYED ",
					padx=15,
					pady=15,
					bg="black",
                    font="Arial 25",
					fg="darkgoldenrod")
	head_label.grid(row=0,
					column=0,
					pady=10,
					padx=15,
					columnspan=3)

	link_label = Label(root,
					text="YouTube link : >>>> ",
					font="Arial 14",
					bg="black",
					pady=5,
                    fg="darkgoldenrod",
					padx=5)
	link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)

	root.linkText = Entry(root,
						width=35,
						textvariable=video_Link,
						font="Arial 14")
	root.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)

	browse_A = Button(root,
					text="paste",
					command=update_text,
					width=10,
					bg="black",
                    fg="darkgoldenrod",
					relief=GROOVE)
	browse_A.grid(row=2,
				column=3,
				pady=1,
				padx=1)

	destination_label = Label(root,
							text="Download location : >>>>",
							font="Arial 14",
							bg="black",
                            fg="darkgoldenrod",
							pady=5,
							padx=9)
	destination_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


	root.destinationText = Entry(root,
								width=27,
								textvariable=download_Path,
								font="Arial 14")
	root.destinationText.grid(row=3,
							column=1,
							pady=5,
							padx=5)



	browse_B = Button(root,
					text="Browse",
					command=Browse,
					width=10,
					bg="black",
                    fg="darkgoldenrod",
					relief=GROOVE)
	browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)

	Download_B = Button(root,
						text="Download Video",
						command=Download,
						width=20,
						bg="black",
                        fg="darkgoldenrod",
						pady=10,
						padx=15,
						relief=GROOVE,
						font="Arial, 14")
	Download_B.grid(row=4,
					column=0,
					pady=10,
					padx=10)
	Download_C = Button(root,
						text="Download Audio",
						command=Downloader,
						width=20,
						bg="black",
                        fg="darkgoldenrod",
						pady=10,
						padx=15,
						relief=GROOVE,
						font="Arial, 14")
	Download_C.grid(row=5,
					column=0,
					pady=20,
					padx=20)



def update_text():
   global linkText 
   root.linkText.insert(END,pyperclip.paste())

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
	videoStream = getVideo.streams.get_by_itag(18)

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

root = tk.Tk()


root.geometry("790x380")
root.resizable(False, False)
root.title("MOHAMED ELSAYED")
root.config(background="black")

# Creating the tkinter Variables

video_Link = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application

root.mainloop()

