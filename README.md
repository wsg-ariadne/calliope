# Calliope
📜 Language clarity model for [Ariadne](https://github.com/wsg-ariadne/ariadne).

Janus is a Naive-Bayes classifier that is meant to process the text from a cookie banner and classify it into the following classes:

1. `GOOD` indicating that the language used in the extract is likely to be clear, descriptive, and provides options to provide or deny cookie consent
2. `BAD` indicating that the language used in the extract is likely to be confusing, vague, and assuming that cookie consent will be provided

This classifier allows [Ariadne](https://github.com/wsg-ariadne/ariadne) to determine whether a website uses deceptive design in the form of unclear language on its cookie banner.

## Usage

### Requirements
Install Python 3.8+ (tested on 3.8.16) and the packages in `requirements.txt` using `pip install -r requirements.txt`.

### Generating the model
Run `python generate.py` to generate the model, save the model as a pickle, and test the pickled model.

### Using the model
Run `python test.py` to have the program provide an opportunity to input text and provide more explicit output regarding the result.

## Details on the Model