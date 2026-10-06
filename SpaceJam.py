from direct.showbase.ShowBase import ShowBase
import math, sys, random

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")

        self.Universe.reparentTo(self.render)

        self.Universe.setScale(15000)

        Planet2_texture = self.loader.loadTexture("./Assets/Planets/images.jpeg")
        self.Planet2 = self.loader.loadModel("models/misc/sphere")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setTexture(Planet2_texture, 1)
        self.Planet2.setPos(150, 2500, 67)
        self.Planet2.setScale(350)



        # Load a planet image as a texture
        Planet1_texture = self.loader.loadTexture("./Assets/Planets/images.jpeg")
        self.Planet1 = self.loader.loadModel("models/misc/sphere")
        self.Planet1.reparentTo(self.render)
        # Apply the JPEG texture to the sphere
        self.Planet1.setTexture(Planet1_texture, 1)
        self.Planet1.setPos(150, 3000, 67)
        self.Planet1.setScale(350)

        Planet3_texture = self.loader.loadTexture("./Assets/Planets/images.jpeg")
        self.Planet3 = self.loader.loadModel("models/misc/sphere")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setTexture(Planet3_texture, 1)
        self.Planet3.setPos(150, 3500, 67)
        self.Planet3.setScale(350)

        Planet4_texture = self.loader.loadTexture("./Assets/Planets/images.jpeg")
        self.Planet4 = self.loader.loadModel("models/misc/sphere")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setTexture(Planet4_texture, 1)
        self.Planet4.setPos(150, 4000, 67)
        self.Planet4.setScale(350)

        Planet5_texture = self.loader.loadTexture("./Assets/Planets/images.jpeg")
        self.Planet5 = self.loader.loadModel("models/misc/sphere")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setTexture(Planet5_texture, 1)
        self.Planet5.setPos(150, 4500, 67)
        self.Planet5.setScale(350)

        Planet6_texture = self.loader.loadTexture("./Assets/Planets/images.jpeg")
        self.Planet6 = self.loader.loadModel("models/misc/sphere")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setTexture(Planet6_texture, 1)
        self.Planet6.setPos(150, 5000, 67)
        self.Planet6.setScale(350)

        tex = self.loader.loadTexture("./Assets/Universe/images-1.jpeg")
        self.Universe.setTexture(tex, 1)


app = MyApp()
app.run()

#Link for planet picture https://www.nbcnews.com/mach/science/what-dwarf-planet-ncna926751
#Link for planet picture - image 6 - https://www.nhm.ac.uk/discover/planet-mercury.html
#Link for planet picture - image 2 - https://esawebb.org/wordbank/planet/
#Link for planet picture - image 3 - https://www.sciencedaily.com/releases/2026/01/260101160859.htm
#Link for planet picture - image 4 - https://www.space.com/25986-planet-definition.html
#Link for planet picture - image 5 - https://www.wired.com/story/scientists-scan-mysterious-planet-as-it-drifts-through-space/
#Universe picture https://www.newscientist.com/article/2524208-100-year-old-assumption-about-the-universe-may-soon-be-overturned/
#Space ship - https://www.artstation.com/artwork/YqvZq