### Goal:

- store images on cassette tapes

## Overall plan:

- Implement an efficient algorithm to turn images into 1bit depth images (done)

- generate an audio signal that represents the image

# How to use:

```python
# open "floyed-Steinberg dishering.py" with the text editor of your choice
# edit the line 54 so it points to the desired file
image = Image.open("./Static/YOURFILE.jpg").convert("L")
# make sure the path is correct, you'll also need to install pandas and jit
#RUN!
```

