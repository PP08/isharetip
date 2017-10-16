import dropbox

dbx = dropbox.Dropbox('gI80eXO4ucUAAAAAAAADXUMbrld8uZvAxPlQzEVyJedbPflaUda9L-8Bub7DY1JW')
# dbx.files_upload("Potential headline: Game 5 a nail-biter as Warriors inch out Cavs", '/test/game5/story.txt')
dbx.files_upload('manage.py', '/hello.txt')