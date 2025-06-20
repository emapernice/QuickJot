import notes.note as model

class Actions:

    def create(self, user):
        print(f"\nOk {user[1]}!! Let's create a new note...")

        title = input("Enter the title of the note: ")
        description = input("Enter the description of the note: ")

        note = model.Note(user[0], title, description)
        save = note.save()

        if save[0] >= 1:
            print(f"\nPerfect, you have saved the note: {note.title}")

        else:
            print(f"\nSorry, the note was not saved {user[1]}")   

    def show(self, user):
        print(f"\nOkay, {user[1]}. Here are your notes: ")   

        note = model.Note(user[0])     
        notes = note.show() 

        for note in notes:
            print("\n**********************************************")
            print(note[2])
            print(note[3])
            print("\n**********************************************")

    def delete(self, user):
        print(f"\nOkay {user[1]}!! Let's delete notes.")     

        title = input("Enter the title of the note to be deleted: ")  

        note = model.Note(user[0], title)
        delete = note.delete()

        if delete[0] >= 1:
            print(f"The note has been deleted: {note.title}")

        else:
            print("The note hasn't been deleted, please try again later...")     