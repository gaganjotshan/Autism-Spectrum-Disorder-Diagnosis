## Gameplan
-  3 minutes time divided by 3 people
-  Sections to talk about
	1. Introduction and Objectives
	2. ABIDE-II, Preprocessing and initial results
	3. Final Results and improvements
*  Writing
	*  Use thesaurus
	*  Use words from the malis course page
-  Which order to go with (my suggestion)
	1. Dario
	2. Gaganjot
	3. Giulia


_"Presentations will be graded based on their quality and clarity, the technical content, and the knowledge demonstrated by the team when discussing the work with the jury members"  - Maria_

## Sections

### Section 1: Introduction and Objectives

- Good morning and thank you for being here.
- The main problem we tackled during our final project has been the application of Machine Learning Classifiers to the task of Autism Spectrum Disorder diagnosis.
- In our project we want to give a contribution to the challenge of ASD diagnosis by providing a model that would work reasonably well with M/F subs
- We wanted to try a different approach from the research we've seen, where normally female samples are excluded because of the very different neuropathology between the two sexes, plus the significant imbalance between the samples available
- We decided to use resting-state fMRI data obtained from the ABIDE-II project, taking as many males as females available, and an equal number of Autistic and Control samples.
- To start, we adopted the automated preprocessing pipeline CPAC, which helped us apply alignment, de-noising and other operations to the images.

### Section 2: Initial attempts

- We encountered a huge roadblock when we realized that the preprocessed images, which were represented by 4D vectors, were too big to fit in RAM: the entire dataset was more than 100GB.
- We then decided to look into feature extraction methods, and we found that among the output of our preprocessing pipeline we already had correlation matrices generated by performing Region of Interest processing with a 200 ROI Craddock Atlas.
- Unfortunately, this step had failed for some subjects, leaving us with an even more reduced dataset than the already small one we had started with. This probably contributed to an overall poor performance of our baseline model.

 ### Section 3:  Final Results

 - Performance Improvement
	 - Hyperparameter tuning:  nested 5-fold C.V. 
- Manually generated the Corr. Matrixes -> data for all of the subjects
- Fit LogReg and SVM on those obtained
- We immediately saw that the performance was getting better, so we continued with more hyperparameter tuning to reach a final performance of 0.57 with both models
- We also tested separately with samples of only Males / Females to compare the performances, and as we can see from the graph the performance varies a lot: in particular if a model performs well on Males it will badly on Females and vice-versa. 
