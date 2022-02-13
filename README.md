# KwaiRec: A Fully Observed Dataset for Recommender Systems (Density: Almost 100%)

[![LICENSE](https://img.shields.io/badge/license-CC--BY--4.0-green)](https://github.com/chongminggao/KwaiRec/blob/main/LICENSE)

*KwaiRec* is a real-world dataset collected from the recommendation logs of the video-sharing mobile app [Kwai](https://www.kwai.com/). For now, it is the first dataset that contains a fully observed user-item interaction matrix. For the term "fully observed", we mean there are almost no missing values in the user-item matrix,  i.e., each user has viewed each video and then leaved feedback. 

The following figure illustrates the user-item matrices in traditional datasets and *KwaiRec*.

![kwaidata](https://raw.githubusercontent.com/chongminggao/KwaiRec/main/figs/KwaiRec.png)

With all user's preference known, KwaiRec can used in offline evaluation (i.e., offline A/B test) for recommendation models. It can benefit lots of research directions, such as unbiased recommendation, interactive/conversational recommendation, or reinforcement learning (RL) and off-policy evaluation (OPE) for recommendation.

If you use it in your work, please cite our paper:
 [![LINK](https://img.shields.io/badge/-Paper%20Link-lightgrey)](#) [![PDF](https://img.shields.io/badge/-PDF-red)](#)

> arxiv: todo

[This repository](https://github.com/xiwenchao/fully_observed_demo) lists the example codes in evaluating conversational recommendation as descripted in the paper.

---

## Download the data

We provides several options to download this dataset:

  1. Download mannually through the following links:

     - Optional link 1: [Google Drive](https://drive.google.com/file/d/1-ZZ4d3GtPb5fwxGsdQ6Dti09dhEy23Mm/view?usp=sharing)

     - Optional link 2: [USTC Drive](https://rec.ustc.edu.cn/share/de0098e0-8c9e-11ec-a7fd-37f9e83716e7)

  2. Download using the "wget" command.

     ```shell
     wget https://linux.chongminggao.top/data/KwaiRec.zip
     ```


The script `loaddata.py` provides a simple way to load the data via Pandas in Python.

---

## Data Descriptions

*KwaiRec* contains millions of user-item interactions as well as the side information include the item categorires and social network. Four files are included in the download data: 

  ```shell
  .
  ├── data
  │   ├── big_matrix.csv          
  │   ├── small_matrix.csv
  │   ├── social_network.csv
  │   └── item_categories.csv
  ```

The statistics of the small matrix and big matrix in *KwaiRec*.

|                | #Users | #Items | #Interactions | #Attributes of items | #Users who have friends | Density |
| -------------- | :----: | :----: |  :----: | :------------------: | :---------------------: | :-----: |
| *small matrix* | 1,411  | 3,327  | 4,676,570 |          31          | 146 |  99.6%  |
| *big matrix*   | 7,176  | 10,729 | 12,530,806 |          31          | 472 | 16.3% |

Note that the density of small matrix is 99.6% instead of 100% because some users have explicitly indicated that they would not be willing to receive recommendations from certain authors. I.e., They blocked these videos.

#### 1. Descriptions of the fields in `big_matrix.csv` and `small_matrix.csv`. 

| Field Name:    | Description                                              | Type    | Example                   |
| -------------- | -------------------------------------------------------- | ------- | ------------------------- |
| user_id        | The ID of the user.                                      | int64   | 0                         |
| photo_id       | The ID of the viewed video.                              | int64   | 3650                      |
| play_duration  | Time of video viewing of this interaction (millisecond). | int64   | 13838                     |
| photo_duration | Time of this video (millisecond).                        | int64   | 10867                     |
| time           | Human-readable date for this interaction                 | str     | "2020-07-05 00:08:23.438" |
| date           | Date of this interaction                                 | int64   | 20200705                  |
| timestamp      | Unix timestamp                                           | float64 | 1593878903.438            |
| watch_ratio    | The video watching ratio (=play_duration/photo_duration) | float64 | 1.273397                  |

The "watch_ratio" can be deemed as the label of the interaction. Note: there is no "like" signal for this dataset. If you need this binary signal in your scenarios, you can create it yourself. E.g., `like = 1 if watch_ratio > 2.0`.

#### 2. Descriptions of the fields in `social_network.csv`

| Field Name: | Description                                 | Type  | Example     |
| ----------- | ------------------------------------------- | ----- | ----------- |
| user_id     | The ID of the user.                         | int64 | 5352        |
| friend_list | The list of ID of the friends of this user. | list  | [4202,7126] |

#### 3. Descriptions of the fields in `item_categories.csv`. 

| Field Name: | Description                     | Type  | Example |
| ----------- | ------------------------------- | ----- | ------- |
| photo_id    | The ID of the video.            | int64 | 1       |
| feat        | The list of tags of this video. | list  | [27,9]  |
