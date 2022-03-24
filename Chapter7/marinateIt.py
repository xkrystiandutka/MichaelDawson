# Marinate it
# Demonstrates marinating and shelving

import pickle, shelve

print("Marinating list.")
variety = ["mild", "spicy", "pickled"]
shape = ["whole", "sliced lengthwise", "sliced"]
brand = ["Dawtona", "Klimex", "Vortumnus"]
f = open("Chapter7/pickle/pickle1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("Pickling list.")
f = open("Chapter7/pickle/pickle1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print("Putting the lists on the shelf.")
s = shelve.open("Chapter7/pickle/pickles2.dat")
s["variety"] = ["mild", "spicy", "pickled"]
s['shape'] = ['whole', 'cut lengthwise', 'sliced']
s["brand"] = ["Dawtona", "Klimex", "Vortumnus"]
s.sync() # make sure the data is saved

print("Downloading lists from shelf file:")
print("brand -", s["brand"])
print('shape -', s['shape'])
print('variety -', s['variety'])
s.close()

input("To exit the program, press enter.")

