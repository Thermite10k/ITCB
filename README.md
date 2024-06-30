### Goal:

- store images on cassette tapes
- transmitt images through FM a transmitter

## Overall plan:

- Implement efficient algorithms to turn images into 1bit depth images
- Turn the 1bit image to an array consiting of 0s and 1s
- Turn that array into a sound file
- store/save

# How to use:

```python
# open "floyed-Steinberg dishering.py" with the text editor of your choice
# edit the line 54 so it points to the desired file
image = Image.open("./Static/YOURFILE.jpg").convert("L")
# make sure the path is correct, you'll also need to install pandas and jit
#RUN!
```
