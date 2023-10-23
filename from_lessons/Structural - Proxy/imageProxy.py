"""
- ImageProxy può essere usata al posto di Image.Image. Basta usare qualsiasi interfaccia che supporti Image.
- Un oggetto ImageProxy non salva un’immagine ma mantiene una lista di tuple di comandi dove il primo elemento di ciascuna tupla è una funzione od un metodo unbound ed i rimanenti elementi sono gli argomenti da passare quando la funzione o il metodo è invocato
- ImageProxy supporta pienamente i 4 metodi di Image.Image line(), rectangle(), ellipse() e set_pixel(). Ogni volta che ne viene invocato uno, questo è aggiunto in una lista di comandi.
- Solo quando si sceglie di salvare l’immagine, questa viene effettivamente creata e vengono eseguite tutte le funzioni nel buffer.
- Se un metodo non supportato viene invocato (come pixel()) Python lancia AttributeError.
- Alternativamente, creiamo una vera immagine non appena uno di questi metodi è invocato, così userà la vera immagine per l’esecuzione.
- È utile compore l’immagine solo alla fine dell’esecuzione perché:
    - 1) non è detto che ci arrivi
    - 2) è sicuramente necessario lo sforzo richiesto alla macchina.
"""
class ImageProxy:
	def __init__(self, ImageClass, width=None, height=None, filename=None):
		assert (width is not None and height is not None) or \
		 filename is not None
	 self.Image = ImageClass
	 self.commands = []
	if filename is not None:
	 self.load(filename)
	else:
	 self.commands = [(self.Image, width, height)]

	def load(self, filename):
	 self.commands = [(self.Image, None, None, filename)]
	def set_pixel(self, x, y, color):
	 self.commands.append((self.Image.set_pixel, x, y, color))
	def line(self, x0, y0, x1, y1, color):
	 self.commands.append((self.Image.line, x0, y0, x1, y1, color))
	def rectangle(self, x0, y0, x1, y1, outline=None, fill=None):
	 self.commands.append((self.Image.rectangle, x0, y0, x1, y1, outline, fill))
	def ellipse(self, x0, y0, x1, y1, outline=None, fill=None):
	 self.commands.append((self.Image.ellipse, x0, y0, x1, y1, outline, fill))

	def save(self, filename=None):
		command = self.commands.pop[0]
		function, *args = command
		image = function(*args)
		for command in self.commands:
			function, *args = command
			function(image, *args)
		image.save(filename)
		return image
