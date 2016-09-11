from mongoengine import connect, Document, StringField, IntField

class Shape(Document):
    name = StringField()
    sides = IntField()

if __name__ == '__main__':
    connect('hellopython')
    square = Shape('square', 4)
    octagon = Shape('octagon', 8)
    circle = Shape('circle', 1)
    point = Shape('point', 0)

    square.save()
    octagon.save()
    circle.save()
    point.save()
    

    