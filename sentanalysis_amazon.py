{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package vader_lexicon to\n",
      "[nltk_data]     C:\\Users\\saswat\\AppData\\Roaming\\nltk_data...\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nltk.download('vader_lexicon')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.sentiment.vader import SentimentIntensityAnalyzer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "sid = SentimentIntensityAnalyzer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "txt = \"That was the worst movie I had ever seen!!!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'neg': 0.415, 'neu': 0.585, 'pos': 0.0, 'compound': -0.7163}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sid.polarity_scores(txt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('TextFiles/amazonreviews.tsv',sep='\\t')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>label</th>\n",
       "      <th>review</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>pos</td>\n",
       "      <td>Stuning even for the non-gamer: This sound tra...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>pos</td>\n",
       "      <td>The best soundtrack ever to anything.: I'm rea...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>pos</td>\n",
       "      <td>Amazing!: This soundtrack is my favorite music...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>pos</td>\n",
       "      <td>Excellent Soundtrack: I truly like this soundt...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>pos</td>\n",
       "      <td>Remember, Pull Your Jaw Off The Floor After He...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  label                                             review\n",
       "0   pos  Stuning even for the non-gamer: This sound tra...\n",
       "1   pos  The best soundtrack ever to anything.: I'm rea...\n",
       "2   pos  Amazing!: This soundtrack is my favorite music...\n",
       "3   pos  Excellent Soundtrack: I truly like this soundt...\n",
       "4   pos  Remember, Pull Your Jaw Off The Floor After He..."
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "label     0\n",
       "review    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "blanks = []\n",
    "for i,lb,rv in df.itertuples():\n",
    "    if type(rv) == str:\n",
    "        if rv.isspace():\n",
    "            blanks.append(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "blanks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'neg': 0.088, 'neu': 0.669, 'pos': 0.243, 'compound': 0.9454}"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sid.polarity_scores(df.iloc[0]['review'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Stuning even for the non-gamer: This sound track was beautiful! It paints the senery in your mind so well I would recomend it even to people who hate vid. game music! I have played the game Chrono Cross but out of all of the games I have ever played it has the best music! It backs away from crude keyboarding and takes a fresher step with grate guitars and soulful orchestras. It would impress anyone who cares to listen! ^_^'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[0]['review']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['scores'] = df['review'].apply(lambda review:sid.polarity_scores(review))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>label</th>\n",
       "      <th>review</th>\n",
       "      <th>scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>pos</td>\n",
       "      <td>Stuning even for the non-gamer: This sound tra...</td>\n",
       "      <td>{'neg': 0.088, 'neu': 0.669, 'pos': 0.243, 'co...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>pos</td>\n",
       "      <td>The best soundtrack ever to anything.: I'm rea...</td>\n",
       "      <td>{'neg': 0.018, 'neu': 0.837, 'pos': 0.145, 'co...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>pos</td>\n",
       "      <td>Amazing!: This soundtrack is my favorite music...</td>\n",
       "      <td>{'neg': 0.04, 'neu': 0.692, 'pos': 0.268, 'com...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>pos</td>\n",
       "      <td>Excellent Soundtrack: I truly like this soundt...</td>\n",
       "      <td>{'neg': 0.09, 'neu': 0.615, 'pos': 0.295, 'com...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>pos</td>\n",
       "      <td>Remember, Pull Your Jaw Off The Floor After He...</td>\n",
       "      <td>{'neg': 0.0, 'neu': 0.746, 'pos': 0.254, 'comp...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  label                                             review  \\\n",
       "0   pos  Stuning even for the non-gamer: This sound tra...   \n",
       "1   pos  The best soundtrack ever to anything.: I'm rea...   \n",
       "2   pos  Amazing!: This soundtrack is my favorite music...   \n",
       "3   pos  Excellent Soundtrack: I truly like this soundt...   \n",
       "4   pos  Remember, Pull Your Jaw Off The Floor After He...   \n",
       "\n",
       "                                              scores  \n",
       "0  {'neg': 0.088, 'neu': 0.669, 'pos': 0.243, 'co...  \n",
       "1  {'neg': 0.018, 'neu': 0.837, 'pos': 0.145, 'co...  \n",
       "2  {'neg': 0.04, 'neu': 0.692, 'pos': 0.268, 'com...  \n",
       "3  {'neg': 0.09, 'neu': 0.615, 'pos': 0.295, 'com...  \n",
       "4  {'neg': 0.0, 'neu': 0.746, 'pos': 0.254, 'comp...  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['compound_scores'] = df['scores'].apply(lambda d:d['compound'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>label</th>\n",
       "      <th>review</th>\n",
       "      <th>scores</th>\n",
       "      <th>compound_scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>pos</td>\n",
       "      <td>Stuning even for the non-gamer: This sound tra...</td>\n",
       "      <td>{'neg': 0.088, 'neu': 0.669, 'pos': 0.243, 'co...</td>\n",
       "      <td>0.9454</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>pos</td>\n",
       "      <td>The best soundtrack ever to anything.: I'm rea...</td>\n",
       "      <td>{'neg': 0.018, 'neu': 0.837, 'pos': 0.145, 'co...</td>\n",
       "      <td>0.8957</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>pos</td>\n",
       "      <td>Amazing!: This soundtrack is my favorite music...</td>\n",
       "      <td>{'neg': 0.04, 'neu': 0.692, 'pos': 0.268, 'com...</td>\n",
       "      <td>0.9858</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>pos</td>\n",
       "      <td>Excellent Soundtrack: I truly like this soundt...</td>\n",
       "      <td>{'neg': 0.09, 'neu': 0.615, 'pos': 0.295, 'com...</td>\n",
       "      <td>0.9814</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>pos</td>\n",
       "      <td>Remember, Pull Your Jaw Off The Floor After He...</td>\n",
       "      <td>{'neg': 0.0, 'neu': 0.746, 'pos': 0.254, 'comp...</td>\n",
       "      <td>0.9781</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  label                                             review  \\\n",
       "0   pos  Stuning even for the non-gamer: This sound tra...   \n",
       "1   pos  The best soundtrack ever to anything.: I'm rea...   \n",
       "2   pos  Amazing!: This soundtrack is my favorite music...   \n",
       "3   pos  Excellent Soundtrack: I truly like this soundt...   \n",
       "4   pos  Remember, Pull Your Jaw Off The Floor After He...   \n",
       "\n",
       "                                              scores  compound_scores  \n",
       "0  {'neg': 0.088, 'neu': 0.669, 'pos': 0.243, 'co...           0.9454  \n",
       "1  {'neg': 0.018, 'neu': 0.837, 'pos': 0.145, 'co...           0.8957  \n",
       "2  {'neg': 0.04, 'neu': 0.692, 'pos': 0.268, 'com...           0.9858  \n",
       "3  {'neg': 0.09, 'neu': 0.615, 'pos': 0.295, 'com...           0.9814  \n",
       "4  {'neg': 0.0, 'neu': 0.746, 'pos': 0.254, 'comp...           0.9781  "
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['comp_score'] = df['compound_scores'].apply(lambda s:'pos' if s>=0 else 'neg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>label</th>\n",
       "      <th>review</th>\n",
       "      <th>scores</th>\n",
       "      <th>compound_scores</th>\n",
       "      <th>comp_score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>pos</td>\n",
       "      <td>Stuning even for the non-gamer: This sound tra...</td>\n",
       "      <td>{'neg': 0.088, 'neu': 0.669, 'pos': 0.243, 'co...</td>\n",
       "      <td>0.9454</td>\n",
       "      <td>pos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>pos</td>\n",
       "      <td>The best soundtrack ever to anything.: I'm rea...</td>\n",
       "      <td>{'neg': 0.018, 'neu': 0.837, 'pos': 0.145, 'co...</td>\n",
       "      <td>0.8957</td>\n",
       "      <td>pos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>pos</td>\n",
       "      <td>Amazing!: This soundtrack is my favorite music...</td>\n",
       "      <td>{'neg': 0.04, 'neu': 0.692, 'pos': 0.268, 'com...</td>\n",
       "      <td>0.9858</td>\n",
       "      <td>pos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>pos</td>\n",
       "      <td>Excellent Soundtrack: I truly like this soundt...</td>\n",
       "      <td>{'neg': 0.09, 'neu': 0.615, 'pos': 0.295, 'com...</td>\n",
       "      <td>0.9814</td>\n",
       "      <td>pos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>pos</td>\n",
       "      <td>Remember, Pull Your Jaw Off The Floor After He...</td>\n",
       "      <td>{'neg': 0.0, 'neu': 0.746, 'pos': 0.254, 'comp...</td>\n",
       "      <td>0.9781</td>\n",
       "      <td>pos</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  label                                             review  \\\n",
       "0   pos  Stuning even for the non-gamer: This sound tra...   \n",
       "1   pos  The best soundtrack ever to anything.: I'm rea...   \n",
       "2   pos  Amazing!: This soundtrack is my favorite music...   \n",
       "3   pos  Excellent Soundtrack: I truly like this soundt...   \n",
       "4   pos  Remember, Pull Your Jaw Off The Floor After He...   \n",
       "\n",
       "                                              scores  compound_scores  \\\n",
       "0  {'neg': 0.088, 'neu': 0.669, 'pos': 0.243, 'co...           0.9454   \n",
       "1  {'neg': 0.018, 'neu': 0.837, 'pos': 0.145, 'co...           0.8957   \n",
       "2  {'neg': 0.04, 'neu': 0.692, 'pos': 0.268, 'com...           0.9858   \n",
       "3  {'neg': 0.09, 'neu': 0.615, 'pos': 0.295, 'com...           0.9814   \n",
       "4  {'neg': 0.0, 'neu': 0.746, 'pos': 0.254, 'comp...           0.9781   \n",
       "\n",
       "  comp_score  \n",
       "0        pos  \n",
       "1        pos  \n",
       "2        pos  \n",
       "3        pos  \n",
       "4        pos  "
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score,classification_report,confusion_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.7091\n"
     ]
    }
   ],
   "source": [
    "print(accuracy_score(df['label'],df['comp_score']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "         neg       0.86      0.51      0.64      5097\n",
      "         pos       0.64      0.91      0.75      4903\n",
      "\n",
      "   micro avg       0.71      0.71      0.71     10000\n",
      "   macro avg       0.75      0.71      0.70     10000\n",
      "weighted avg       0.75      0.71      0.70     10000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(df['label'],df['comp_score']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2623 2474]\n",
      " [ 435 4468]]\n"
     ]
    }
   ],
   "source": [
    "print(confusion_matrix(df['label'],df['comp_score']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
