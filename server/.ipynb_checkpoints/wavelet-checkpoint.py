{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fcf5c6ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\yigit\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\scipy\\__init__.py:146: UserWarning: A NumPy version >=1.17.3 and <1.25.0 is required for this version of SciPy (detected version 1.26.2\n",
      "  warnings.warn(f\"A NumPy version >={np_minversion} and <{np_maxversion}\"\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pywt\n",
    "import cv2\n",
    "\n",
    "def w2d(img, mode='haar', level=1):\n",
    "    imArray = img\n",
    "    #Datatype conversions\n",
    "    #convert to grayscale\n",
    "    imArray = cv2.cvtColor( imArray,cv2.COLOR_RGB2GRAY )\n",
    "    #convert to float\n",
    "    imArray =  np.float32(imArray)\n",
    "    imArray /= 255;\n",
    "    # compute coefficients\n",
    "    coeffs=pywt.wavedec2(imArray, mode, level=level)\n",
    "\n",
    "    #Process Coefficients\n",
    "    coeffs_H=list(coeffs)\n",
    "    coeffs_H[0] *= 0;\n",
    "\n",
    "    # reconstruction\n",
    "    imArray_H=pywt.waverec2(coeffs_H, mode);\n",
    "    imArray_H *= 255;\n",
    "    imArray_H =  np.uint8(imArray_H)\n",
    "\n",
    "    return imArray_H"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "798e2774",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
