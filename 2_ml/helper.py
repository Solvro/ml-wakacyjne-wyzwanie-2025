import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()


def proces_df(titanic_df):
    # obsługa wieku
    for sex in ['female', 'male']:
        for pclass in [1, 2, 3]:
            median_age = titanic_df.loc[
                (titanic_df['Sex'] == sex) & (titanic_df['Pclass'] == pclass),
                'Age'
            ].median()

            titanic_df.loc[
                (titanic_df['Sex'] == sex) & (titanic_df['Pclass'] == pclass),
                'Age'
            ] = titanic_df.loc[
                (titanic_df['Sex'] == sex) & (titanic_df['Pclass'] == pclass),
                'Age'
            ].fillna(median_age)

    # obsłużenie ceny biletu
    titanic_df['Fare'] = titanic_df['Fare'].fillna(titanic_df.Fare.mean())

    # obsłużenie cabin
    titanic_df['Cabin'] = titanic_df['Cabin'].fillna("Not Stated")

    # obsłużenie embarked
    titanic_df['Embarked'] = titanic_df['Embarked'].fillna("S")

    titanic_df['Survived'] = titanic_df['Survived'].astype('category')
    titanic_df['Pclass'] = titanic_df['Pclass'].astype('category')
    # to samo z sex
    titanic_df['Sex'] = titanic_df['Sex'].astype('category')
    titanic_df['SibSp'] = titanic_df['SibSp'].astype('category')
    titanic_df['Parch'] = titanic_df['Parch'].astype('category')
    titanic_df['Cabin'] = titanic_df['Cabin'].astype('category')

    # nowe kolumny
    titanic_df['Department'] = titanic_df['Cabin'].str[0]  # Wartość 'N' jest po Not stated może się przyda

    titanic_df['AgeGroup'] = np.where(titanic_df['Age'] <= 12, 'child',
                                      np.where(titanic_df['Age'] <= 17, 'teenager',
                                               np.where(titanic_df['Age'] <= 60, 'adult', 'elderly')))
    titanic_df['TicketPrice'] = np.where(titanic_df['Fare'] == 0, 'free',
                                         np.where(titanic_df['Fare'] <= 11, 'low',
                                                  np.where(titanic_df['Fare'] <= 100, 'medium', 'high')))

    mapping_sex = {
        'female': 0,
        'male': 1,
    }

    mapping_embarked = {
        'S': 0,
        'C': 1,
        'Q': 2
    }

    mapping_department = {
        'N': 0,
        'C': 1,
        'B': 2,
        'D': 3,
        'E': 4,
        'A': 5,
        'F': 6,
        'G': 7,
        'T': 8
    }

    mapping_age_group = {
        'child': 0,
        'teenager': 1,
        'adult': 2,
        'elderly': 3
    }

    mapping_ticket_price = {
        'free': 0,
        'low': 1,
        'medium': 2,
        'high': 3
    }

    titanic_df['Sex'] = titanic_df['Sex'].map(mapping_sex)
    titanic_df['Embarked'] = titanic_df['Embarked'].map(mapping_embarked)
    titanic_df['Department'] = titanic_df['Department'].map(mapping_department)
    titanic_df['AgeGroup'] = titanic_df['AgeGroup'].map(mapping_age_group)
    titanic_df['TicketPrice'] = titanic_df['TicketPrice'].map(mapping_ticket_price)

    # usuwanie
    titanic_df.drop(columns=["Name", "Ticket", "Cabin"], inplace=True)

    titanic_df[['Fare', 'Age']] = scaler.fit_transform(titanic_df[['Fare', 'Age']])

    return titanic_df
