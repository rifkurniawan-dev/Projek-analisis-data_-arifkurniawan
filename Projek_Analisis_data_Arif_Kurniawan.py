{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rifkurniawan-dev/Projek-analisis-data_-arifkurniawan/blob/main/Projek_Analisis_data_Arif_Kurniawan.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n"
      ],
      "metadata": {
        "id": "3XJf60xunKsL"
      },
      "execution_count": 138,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Gathering**"
      ],
      "metadata": {
        "id": "lU7w9aF-nN8l"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#memuat data\n",
        "day_df= pd.read_csv(\"day.csv\")\n",
        "day_df.head()\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 313
        },
        "id": "BqWy6fbvnXVg",
        "outputId": "89ae2b95-c8d2-4faa-cd22-5241229d6747"
      },
      "execution_count": 139,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   instant      dteday  season  yr  mnth  holiday  weekday  workingday  \\\n",
              "0        1  2011-01-01       1   0     1        0        6           0   \n",
              "1        2  2011-01-02       1   0     1        0        0           0   \n",
              "2        3  2011-01-03       1   0     1        0        1           1   \n",
              "3        4  2011-01-04       1   0     1        0        2           1   \n",
              "4        5  2011-01-05       1   0     1        0        3           1   \n",
              "\n",
              "   weathersit      temp     atemp       hum  windspeed  casual  registered  \\\n",
              "0           2  0.344167  0.363625  0.805833   0.160446     331         654   \n",
              "1           2  0.363478  0.353739  0.696087   0.248539     131         670   \n",
              "2           1  0.196364  0.189405  0.437273   0.248309     120        1229   \n",
              "3           1  0.200000  0.212122  0.590435   0.160296     108        1454   \n",
              "4           1  0.226957  0.229270  0.436957   0.186900      82        1518   \n",
              "\n",
              "    cnt  \n",
              "0   985  \n",
              "1   801  \n",
              "2  1349  \n",
              "3  1562  \n",
              "4  1600  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e2727613-747f-481b-a25c-f1b371e9309e\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>instant</th>\n",
              "      <th>dteday</th>\n",
              "      <th>season</th>\n",
              "      <th>yr</th>\n",
              "      <th>mnth</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>cnt</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0.344167</td>\n",
              "      <td>0.363625</td>\n",
              "      <td>0.805833</td>\n",
              "      <td>0.160446</td>\n",
              "      <td>331</td>\n",
              "      <td>654</td>\n",
              "      <td>985</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>2011-01-02</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0.363478</td>\n",
              "      <td>0.353739</td>\n",
              "      <td>0.696087</td>\n",
              "      <td>0.248539</td>\n",
              "      <td>131</td>\n",
              "      <td>670</td>\n",
              "      <td>801</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>2011-01-03</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.196364</td>\n",
              "      <td>0.189405</td>\n",
              "      <td>0.437273</td>\n",
              "      <td>0.248309</td>\n",
              "      <td>120</td>\n",
              "      <td>1229</td>\n",
              "      <td>1349</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>2011-01-04</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.200000</td>\n",
              "      <td>0.212122</td>\n",
              "      <td>0.590435</td>\n",
              "      <td>0.160296</td>\n",
              "      <td>108</td>\n",
              "      <td>1454</td>\n",
              "      <td>1562</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>2011-01-05</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.226957</td>\n",
              "      <td>0.229270</td>\n",
              "      <td>0.436957</td>\n",
              "      <td>0.186900</td>\n",
              "      <td>82</td>\n",
              "      <td>1518</td>\n",
              "      <td>1600</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e2727613-747f-481b-a25c-f1b371e9309e')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-e2727613-747f-481b-a25c-f1b371e9309e button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-e2727613-747f-481b-a25c-f1b371e9309e');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-e4a4eb65-c573-4c22-b076-61d1d1a29adf\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-e4a4eb65-c573-4c22-b076-61d1d1a29adf')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-e4a4eb65-c573-4c22-b076-61d1d1a29adf button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "day_df",
              "summary": "{\n  \"name\": \"day_df\",\n  \"rows\": 731,\n  \"fields\": [\n    {\n      \"column\": \"instant\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 211,\n        \"min\": 1,\n        \"max\": 731,\n        \"num_unique_values\": 731,\n        \"samples\": [\n          704,\n          34,\n          301\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"dteday\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"num_unique_values\": 731,\n        \"samples\": [\n          \"2012-12-04\",\n          \"2011-02-03\",\n          \"2011-10-28\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"season\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 1,\n        \"max\": 4,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          2,\n          4,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"yr\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"mnth\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3,\n        \"min\": 1,\n        \"max\": 12,\n        \"num_unique_values\": 12,\n        \"samples\": [\n          11,\n          10\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"holiday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"weekday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2,\n        \"min\": 0,\n        \"max\": 6,\n        \"num_unique_values\": 7,\n        \"samples\": [\n          6,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"workingday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"weathersit\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 1,\n        \"max\": 3,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          2,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"temp\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.18305099611148867,\n        \"min\": 0.0591304,\n        \"max\": 0.861667,\n        \"num_unique_values\": 499,\n        \"samples\": [\n          0.544167,\n          0.430435\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"atemp\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.16296117838631127,\n        \"min\": 0.0790696,\n        \"max\": 0.840896,\n        \"num_unique_values\": 690,\n        \"samples\": [\n          0.463375,\n          0.599754\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hum\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.14242909513835394,\n        \"min\": 0.0,\n        \"max\": 0.9725,\n        \"num_unique_values\": 595,\n        \"samples\": [\n          0.707083,\n          0.718333\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"windspeed\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.07749787068166943,\n        \"min\": 0.0223917,\n        \"max\": 0.507463,\n        \"num_unique_values\": 650,\n        \"samples\": [\n          0.100742,\n          0.139308\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"casual\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 686,\n        \"min\": 2,\n        \"max\": 3410,\n        \"num_unique_values\": 606,\n        \"samples\": [\n          709,\n          449\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"registered\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1560,\n        \"min\": 20,\n        \"max\": 6946,\n        \"num_unique_values\": 679,\n        \"samples\": [\n          4531,\n          2553\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"cnt\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1937,\n        \"min\": 22,\n        \"max\": 8714,\n        \"num_unique_values\": 696,\n        \"samples\": [\n          5170,\n          1607\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 139
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#memuat data\n",
        "hour_df= pd.read_csv(\"hour.csv\")\n",
        "hour_df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 313
        },
        "id": "8MhzAm55NRZZ",
        "outputId": "f6687196-6b43-448d-c513-d0323b7ece8b"
      },
      "execution_count": 140,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   instant      dteday  season  yr  mnth  hr  holiday  weekday  workingday  \\\n",
              "0        1  2011-01-01       1   0     1   0        0        6           0   \n",
              "1        2  2011-01-01       1   0     1   1        0        6           0   \n",
              "2        3  2011-01-01       1   0     1   2        0        6           0   \n",
              "3        4  2011-01-01       1   0     1   3        0        6           0   \n",
              "4        5  2011-01-01       1   0     1   4        0        6           0   \n",
              "\n",
              "   weathersit  temp   atemp   hum  windspeed  casual  registered  cnt  \n",
              "0           1  0.24  0.2879  0.81        0.0       3          13   16  \n",
              "1           1  0.22  0.2727  0.80        0.0       8          32   40  \n",
              "2           1  0.22  0.2727  0.80        0.0       5          27   32  \n",
              "3           1  0.24  0.2879  0.75        0.0       3          10   13  \n",
              "4           1  0.24  0.2879  0.75        0.0       0           1    1  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-94c7558a-6908-41bf-93a7-535239086e15\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>instant</th>\n",
              "      <th>dteday</th>\n",
              "      <th>season</th>\n",
              "      <th>yr</th>\n",
              "      <th>mnth</th>\n",
              "      <th>hr</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>cnt</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.81</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>13</td>\n",
              "      <td>16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.22</td>\n",
              "      <td>0.2727</td>\n",
              "      <td>0.80</td>\n",
              "      <td>0.0</td>\n",
              "      <td>8</td>\n",
              "      <td>32</td>\n",
              "      <td>40</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.22</td>\n",
              "      <td>0.2727</td>\n",
              "      <td>0.80</td>\n",
              "      <td>0.0</td>\n",
              "      <td>5</td>\n",
              "      <td>27</td>\n",
              "      <td>32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3</td>\n",
              "      <td>10</td>\n",
              "      <td>13</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>2011-01-01</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>4</td>\n",
              "      <td>0</td>\n",
              "      <td>6</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0.24</td>\n",
              "      <td>0.2879</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-94c7558a-6908-41bf-93a7-535239086e15')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-94c7558a-6908-41bf-93a7-535239086e15 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-94c7558a-6908-41bf-93a7-535239086e15');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-faa3342c-43e9-4506-8472-526e0404df07\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-faa3342c-43e9-4506-8472-526e0404df07')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-faa3342c-43e9-4506-8472-526e0404df07 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "hour_df",
              "summary": "{\n  \"name\": \"hour_df\",\n  \"rows\": 17379,\n  \"fields\": [\n    {\n      \"column\": \"instant\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 5017,\n        \"min\": 1,\n        \"max\": 17379,\n        \"num_unique_values\": 17379,\n        \"samples\": [\n          12831,\n          8689,\n          7092\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"dteday\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"num_unique_values\": 731,\n        \"samples\": [\n          \"2012-12-04\",\n          \"2011-02-03\",\n          \"2011-10-28\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"season\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 1,\n        \"max\": 4,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          2,\n          4,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"yr\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"mnth\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3,\n        \"min\": 1,\n        \"max\": 12,\n        \"num_unique_values\": 12,\n        \"samples\": [\n          11,\n          10\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hr\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6,\n        \"min\": 0,\n        \"max\": 23,\n        \"num_unique_values\": 24,\n        \"samples\": [\n          8,\n          16\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"holiday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"weekday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2,\n        \"min\": 0,\n        \"max\": 6,\n        \"num_unique_values\": 7,\n        \"samples\": [\n          6,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"workingday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"weathersit\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 1,\n        \"max\": 4,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          2,\n          4\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"temp\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.19255612124972407,\n        \"min\": 0.02,\n        \"max\": 1.0,\n        \"num_unique_values\": 50,\n        \"samples\": [\n          0.16,\n          0.82\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"atemp\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.17185021563536587,\n        \"min\": 0.0,\n        \"max\": 1.0,\n        \"num_unique_values\": 65,\n        \"samples\": [\n          0.7879,\n          0.9242\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hum\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.1929298340629125,\n        \"min\": 0.0,\n        \"max\": 1.0,\n        \"num_unique_values\": 89,\n        \"samples\": [\n          0.29,\n          0.61\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"windspeed\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.12234022857279413,\n        \"min\": 0.0,\n        \"max\": 0.8507,\n        \"num_unique_values\": 30,\n        \"samples\": [\n          0.8507,\n          0.4925\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"casual\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 49,\n        \"min\": 0,\n        \"max\": 367,\n        \"num_unique_values\": 322,\n        \"samples\": [\n          201,\n          171\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"registered\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 151,\n        \"min\": 0,\n        \"max\": 886,\n        \"num_unique_values\": 776,\n        \"samples\": [\n          342,\n          744\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"cnt\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 181,\n        \"min\": 1,\n        \"max\": 977,\n        \"num_unique_values\": 869,\n        \"samples\": [\n          594,\n          46\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 140
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Assessing **Data**"
      ],
      "metadata": {
        "id": "UfEIxkRJtAU-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "day_df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L1MWP44srdVF",
        "outputId": "d4c97c0d-47ce-462f-a08a-54c29bd7a710"
      },
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 731 entries, 0 to 730\n",
            "Data columns (total 16 columns):\n",
            " #   Column      Non-Null Count  Dtype  \n",
            "---  ------      --------------  -----  \n",
            " 0   instant     731 non-null    int64  \n",
            " 1   dteday      731 non-null    object \n",
            " 2   season      731 non-null    int64  \n",
            " 3   yr          731 non-null    int64  \n",
            " 4   mnth        731 non-null    int64  \n",
            " 5   holiday     731 non-null    int64  \n",
            " 6   weekday     731 non-null    int64  \n",
            " 7   workingday  731 non-null    int64  \n",
            " 8   weathersit  731 non-null    int64  \n",
            " 9   temp        731 non-null    float64\n",
            " 10  atemp       731 non-null    float64\n",
            " 11  hum         731 non-null    float64\n",
            " 12  windspeed   731 non-null    float64\n",
            " 13  casual      731 non-null    int64  \n",
            " 14  registered  731 non-null    int64  \n",
            " 15  cnt         731 non-null    int64  \n",
            "dtypes: float64(4), int64(11), object(1)\n",
            "memory usage: 91.5+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "day_df.isna().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 586
        },
        "id": "wc0EucHisu8N",
        "outputId": "e2c47e82-ef86-4349-8d0f-210163e24112"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "instant       0\n",
              "dteday        0\n",
              "season        0\n",
              "yr            0\n",
              "mnth          0\n",
              "holiday       0\n",
              "weekday       0\n",
              "workingday    0\n",
              "weathersit    0\n",
              "temp          0\n",
              "atemp         0\n",
              "hum           0\n",
              "windspeed     0\n",
              "casual        0\n",
              "registered    0\n",
              "cnt           0\n",
              "dtype: int64"
            ],
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
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>instant</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>dteday</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>season</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>yr</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mnth</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>holiday</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>weekday</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>workingday</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>weathersit</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>temp</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>atemp</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>hum</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>windspeed</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>casual</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>registered</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>cnt</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 65
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "hour_df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iXY0CFQytPe_",
        "outputId": "8b338c3f-e621-4b99-b9a2-cd46ee2f2b1d"
      },
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 17379 entries, 0 to 17378\n",
            "Data columns (total 17 columns):\n",
            " #   Column      Non-Null Count  Dtype  \n",
            "---  ------      --------------  -----  \n",
            " 0   instant     17379 non-null  int64  \n",
            " 1   dteday      17379 non-null  object \n",
            " 2   season      17379 non-null  int64  \n",
            " 3   yr          17379 non-null  int64  \n",
            " 4   mnth        17379 non-null  int64  \n",
            " 5   hr          17379 non-null  int64  \n",
            " 6   holiday     17379 non-null  int64  \n",
            " 7   weekday     17379 non-null  int64  \n",
            " 8   workingday  17379 non-null  int64  \n",
            " 9   weathersit  17379 non-null  int64  \n",
            " 10  temp        17379 non-null  float64\n",
            " 11  atemp       17379 non-null  float64\n",
            " 12  hum         17379 non-null  float64\n",
            " 13  windspeed   17379 non-null  float64\n",
            " 14  casual      17379 non-null  int64  \n",
            " 15  registered  17379 non-null  int64  \n",
            " 16  cnt         17379 non-null  int64  \n",
            "dtypes: float64(4), int64(12), object(1)\n",
            "memory usage: 2.3+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "hour_df.isna().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 617
        },
        "id": "89P4OM0ktm1q",
        "outputId": "915dcd99-6c1f-4c7c-c0a1-ed35678c287d"
      },
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "instant       0\n",
              "dteday        0\n",
              "season        0\n",
              "yr            0\n",
              "mnth          0\n",
              "hr            0\n",
              "holiday       0\n",
              "weekday       0\n",
              "workingday    0\n",
              "weathersit    0\n",
              "temp          0\n",
              "atemp         0\n",
              "hum           0\n",
              "windspeed     0\n",
              "casual        0\n",
              "registered    0\n",
              "cnt           0\n",
              "dtype: int64"
            ],
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
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>instant</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>dteday</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>season</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>yr</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mnth</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>hr</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>holiday</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>weekday</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>workingday</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>weathersit</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>temp</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>atemp</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>hum</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>windspeed</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>casual</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>registered</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>cnt</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "day_df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 320
        },
        "id": "zHm41L9mttSh",
        "outputId": "284b213f-eeb7-4fda-99d6-e10a40100d28"
      },
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          instant      season          yr        mnth     holiday     weekday  \\\n",
              "count  731.000000  731.000000  731.000000  731.000000  731.000000  731.000000   \n",
              "mean   366.000000    2.496580    0.500684    6.519836    0.028728    2.997264   \n",
              "std    211.165812    1.110807    0.500342    3.451913    0.167155    2.004787   \n",
              "min      1.000000    1.000000    0.000000    1.000000    0.000000    0.000000   \n",
              "25%    183.500000    2.000000    0.000000    4.000000    0.000000    1.000000   \n",
              "50%    366.000000    3.000000    1.000000    7.000000    0.000000    3.000000   \n",
              "75%    548.500000    3.000000    1.000000   10.000000    0.000000    5.000000   \n",
              "max    731.000000    4.000000    1.000000   12.000000    1.000000    6.000000   \n",
              "\n",
              "       workingday  weathersit        temp       atemp         hum   windspeed  \\\n",
              "count  731.000000  731.000000  731.000000  731.000000  731.000000  731.000000   \n",
              "mean     0.683995    1.395349    0.495385    0.474354    0.627894    0.190486   \n",
              "std      0.465233    0.544894    0.183051    0.162961    0.142429    0.077498   \n",
              "min      0.000000    1.000000    0.059130    0.079070    0.000000    0.022392   \n",
              "25%      0.000000    1.000000    0.337083    0.337842    0.520000    0.134950   \n",
              "50%      1.000000    1.000000    0.498333    0.486733    0.626667    0.180975   \n",
              "75%      1.000000    2.000000    0.655417    0.608602    0.730209    0.233214   \n",
              "max      1.000000    3.000000    0.861667    0.840896    0.972500    0.507463   \n",
              "\n",
              "            casual   registered          cnt  \n",
              "count   731.000000   731.000000   731.000000  \n",
              "mean    848.176471  3656.172367  4504.348837  \n",
              "std     686.622488  1560.256377  1937.211452  \n",
              "min       2.000000    20.000000    22.000000  \n",
              "25%     315.500000  2497.000000  3152.000000  \n",
              "50%     713.000000  3662.000000  4548.000000  \n",
              "75%    1096.000000  4776.500000  5956.000000  \n",
              "max    3410.000000  6946.000000  8714.000000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-14ba0b20-a463-4ae4-be6a-4f1c0764b7f6\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>instant</th>\n",
              "      <th>season</th>\n",
              "      <th>yr</th>\n",
              "      <th>mnth</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>cnt</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "      <td>731.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>366.000000</td>\n",
              "      <td>2.496580</td>\n",
              "      <td>0.500684</td>\n",
              "      <td>6.519836</td>\n",
              "      <td>0.028728</td>\n",
              "      <td>2.997264</td>\n",
              "      <td>0.683995</td>\n",
              "      <td>1.395349</td>\n",
              "      <td>0.495385</td>\n",
              "      <td>0.474354</td>\n",
              "      <td>0.627894</td>\n",
              "      <td>0.190486</td>\n",
              "      <td>848.176471</td>\n",
              "      <td>3656.172367</td>\n",
              "      <td>4504.348837</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>211.165812</td>\n",
              "      <td>1.110807</td>\n",
              "      <td>0.500342</td>\n",
              "      <td>3.451913</td>\n",
              "      <td>0.167155</td>\n",
              "      <td>2.004787</td>\n",
              "      <td>0.465233</td>\n",
              "      <td>0.544894</td>\n",
              "      <td>0.183051</td>\n",
              "      <td>0.162961</td>\n",
              "      <td>0.142429</td>\n",
              "      <td>0.077498</td>\n",
              "      <td>686.622488</td>\n",
              "      <td>1560.256377</td>\n",
              "      <td>1937.211452</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.059130</td>\n",
              "      <td>0.079070</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.022392</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>20.000000</td>\n",
              "      <td>22.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>183.500000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.337083</td>\n",
              "      <td>0.337842</td>\n",
              "      <td>0.520000</td>\n",
              "      <td>0.134950</td>\n",
              "      <td>315.500000</td>\n",
              "      <td>2497.000000</td>\n",
              "      <td>3152.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>366.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.498333</td>\n",
              "      <td>0.486733</td>\n",
              "      <td>0.626667</td>\n",
              "      <td>0.180975</td>\n",
              "      <td>713.000000</td>\n",
              "      <td>3662.000000</td>\n",
              "      <td>4548.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>548.500000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.655417</td>\n",
              "      <td>0.608602</td>\n",
              "      <td>0.730209</td>\n",
              "      <td>0.233214</td>\n",
              "      <td>1096.000000</td>\n",
              "      <td>4776.500000</td>\n",
              "      <td>5956.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>731.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>0.861667</td>\n",
              "      <td>0.840896</td>\n",
              "      <td>0.972500</td>\n",
              "      <td>0.507463</td>\n",
              "      <td>3410.000000</td>\n",
              "      <td>6946.000000</td>\n",
              "      <td>8714.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-14ba0b20-a463-4ae4-be6a-4f1c0764b7f6')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-14ba0b20-a463-4ae4-be6a-4f1c0764b7f6 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-14ba0b20-a463-4ae4-be6a-4f1c0764b7f6');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-cd9fb554-07b3-42eb-beb0-c0f704e7a5c4\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-cd9fb554-07b3-42eb-beb0-c0f704e7a5c4')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-cd9fb554-07b3-42eb-beb0-c0f704e7a5c4 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"day_df\",\n  \"rows\": 8,\n  \"fields\": [\n    {\n      \"column\": \"instant\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 263.151210562102,\n        \"min\": 1.0,\n        \"max\": 731.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          731.0,\n          366.0,\n          548.5\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"season\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 257.61068803932375,\n        \"min\": 1.0,\n        \"max\": 731.0,\n        \"num_unique_values\": 7,\n        \"samples\": [\n          731.0,\n          2.496580027359781,\n          3.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"yr\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 258.2457820210964,\n        \"min\": 0.0,\n        \"max\": 731.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.5006839945280438,\n          1.0,\n          0.5003418803818294\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"mnth\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 256.251208377565,\n        \"min\": 1.0,\n        \"max\": 731.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          6.519835841313269,\n          7.0,\n          731.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"holiday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 258.38735524952386,\n        \"min\": 0.0,\n        \"max\": 731.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.028727770177838577,\n          1.0,\n          0.16715474262247393\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"weekday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 257.4447215833011,\n        \"min\": 0.0,\n        \"max\": 731.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          2.997264021887825,\n          3.0,\n          731.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"workingday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 258.23829965962693,\n        \"min\": 0.0,\n        \"max\": 731.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.6839945280437757,\n          1.0,\n          0.46523338667770103\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"weathersit\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 257.94661363848155,\n        \"min\": 0.5448943419593629,\n        \"max\": 731.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          731.0,\n          1.3953488372093024,\n          3.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"temp\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 258.2915817037473,\n        \"min\": 0.0591304,\n        \"max\": 731.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          0.495384788508892,\n          0.498333,\n          731.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"atemp\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 258.2966006263005,\n        \"min\": 0.0790696,\n        \"max\": 731.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          0.47435398864569084,\n          0.486733,\n          731.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hum\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 258.26489554668353,\n        \"min\": 0.0,\n        \"max\": 731.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          0.6278940629274967,\n          0.626667,\n          731.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"windspeed\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 258.37953633824185,\n        \"min\": 0.0223917,\n        \"max\": 731.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          0.190486211627907,\n          0.180975,\n          731.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"casual\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1038.746523887882,\n        \"min\": 2.0,\n        \"max\": 3410.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          848.1764705882352,\n          713.0,\n          731.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"registered\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2266.131168472822,\n        \"min\": 20.0,\n        \"max\": 6946.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          3656.172366621067,\n          3662.0,\n          731.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"cnt\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2862.2176347716063,\n        \"min\": 22.0,\n        \"max\": 8714.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          4504.3488372093025,\n          4548.0,\n          731.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "hour_df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 320
        },
        "id": "2cf3_7zb2N3W",
        "outputId": "71a4f002-f559-4cff-9411-954665cb8fe8"
      },
      "execution_count": 69,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          instant        season            yr          mnth            hr  \\\n",
              "count  17379.0000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean    8690.0000      2.501640      0.502561      6.537775     11.546752   \n",
              "std     5017.0295      1.106918      0.500008      3.438776      6.914405   \n",
              "min        1.0000      1.000000      0.000000      1.000000      0.000000   \n",
              "25%     4345.5000      2.000000      0.000000      4.000000      6.000000   \n",
              "50%     8690.0000      3.000000      1.000000      7.000000     12.000000   \n",
              "75%    13034.5000      3.000000      1.000000     10.000000     18.000000   \n",
              "max    17379.0000      4.000000      1.000000     12.000000     23.000000   \n",
              "\n",
              "            holiday       weekday    workingday    weathersit          temp  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       0.028770      3.003683      0.682721      1.425283      0.496987   \n",
              "std        0.167165      2.005771      0.465431      0.639357      0.192556   \n",
              "min        0.000000      0.000000      0.000000      1.000000      0.020000   \n",
              "25%        0.000000      1.000000      0.000000      1.000000      0.340000   \n",
              "50%        0.000000      3.000000      1.000000      1.000000      0.500000   \n",
              "75%        0.000000      5.000000      1.000000      2.000000      0.660000   \n",
              "max        1.000000      6.000000      1.000000      4.000000      1.000000   \n",
              "\n",
              "              atemp           hum     windspeed        casual    registered  \\\n",
              "count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   \n",
              "mean       0.475775      0.627229      0.190098     35.676218    153.786869   \n",
              "std        0.171850      0.192930      0.122340     49.305030    151.357286   \n",
              "min        0.000000      0.000000      0.000000      0.000000      0.000000   \n",
              "25%        0.333300      0.480000      0.104500      4.000000     34.000000   \n",
              "50%        0.484800      0.630000      0.194000     17.000000    115.000000   \n",
              "75%        0.621200      0.780000      0.253700     48.000000    220.000000   \n",
              "max        1.000000      1.000000      0.850700    367.000000    886.000000   \n",
              "\n",
              "                cnt  \n",
              "count  17379.000000  \n",
              "mean     189.463088  \n",
              "std      181.387599  \n",
              "min        1.000000  \n",
              "25%       40.000000  \n",
              "50%      142.000000  \n",
              "75%      281.000000  \n",
              "max      977.000000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-779d535a-aad7-4985-a1ad-24f6e74804a0\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>instant</th>\n",
              "      <th>season</th>\n",
              "      <th>yr</th>\n",
              "      <th>mnth</th>\n",
              "      <th>hr</th>\n",
              "      <th>holiday</th>\n",
              "      <th>weekday</th>\n",
              "      <th>workingday</th>\n",
              "      <th>weathersit</th>\n",
              "      <th>temp</th>\n",
              "      <th>atemp</th>\n",
              "      <th>hum</th>\n",
              "      <th>windspeed</th>\n",
              "      <th>casual</th>\n",
              "      <th>registered</th>\n",
              "      <th>cnt</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>17379.0000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "      <td>17379.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>8690.0000</td>\n",
              "      <td>2.501640</td>\n",
              "      <td>0.502561</td>\n",
              "      <td>6.537775</td>\n",
              "      <td>11.546752</td>\n",
              "      <td>0.028770</td>\n",
              "      <td>3.003683</td>\n",
              "      <td>0.682721</td>\n",
              "      <td>1.425283</td>\n",
              "      <td>0.496987</td>\n",
              "      <td>0.475775</td>\n",
              "      <td>0.627229</td>\n",
              "      <td>0.190098</td>\n",
              "      <td>35.676218</td>\n",
              "      <td>153.786869</td>\n",
              "      <td>189.463088</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>5017.0295</td>\n",
              "      <td>1.106918</td>\n",
              "      <td>0.500008</td>\n",
              "      <td>3.438776</td>\n",
              "      <td>6.914405</td>\n",
              "      <td>0.167165</td>\n",
              "      <td>2.005771</td>\n",
              "      <td>0.465431</td>\n",
              "      <td>0.639357</td>\n",
              "      <td>0.192556</td>\n",
              "      <td>0.171850</td>\n",
              "      <td>0.192930</td>\n",
              "      <td>0.122340</td>\n",
              "      <td>49.305030</td>\n",
              "      <td>151.357286</td>\n",
              "      <td>181.387599</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.0000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.020000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>4345.5000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.340000</td>\n",
              "      <td>0.333300</td>\n",
              "      <td>0.480000</td>\n",
              "      <td>0.104500</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>34.000000</td>\n",
              "      <td>40.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>8690.0000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.500000</td>\n",
              "      <td>0.484800</td>\n",
              "      <td>0.630000</td>\n",
              "      <td>0.194000</td>\n",
              "      <td>17.000000</td>\n",
              "      <td>115.000000</td>\n",
              "      <td>142.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>13034.5000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.660000</td>\n",
              "      <td>0.621200</td>\n",
              "      <td>0.780000</td>\n",
              "      <td>0.253700</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>220.000000</td>\n",
              "      <td>281.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>17379.0000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>23.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.850700</td>\n",
              "      <td>367.000000</td>\n",
              "      <td>886.000000</td>\n",
              "      <td>977.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-779d535a-aad7-4985-a1ad-24f6e74804a0')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-779d535a-aad7-4985-a1ad-24f6e74804a0 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-779d535a-aad7-4985-a1ad-24f6e74804a0');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-d37c907b-3a48-496b-8910-74e4896b9a15\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-d37c907b-3a48-496b-8910-74e4896b9a15')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-d37c907b-3a48-496b-8910-74e4896b9a15 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"hour_df\",\n  \"rows\": 8,\n  \"fields\": [\n    {\n      \"column\": \"instant\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6263.17088569678,\n        \"min\": 1.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          17379.0,\n          8690.0,\n          13034.5\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"season\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6143.565598544762,\n        \"min\": 1.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 7,\n        \"samples\": [\n          17379.0,\n          2.5016399102364923,\n          3.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"yr\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6144.202229000585,\n        \"min\": 0.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.5025605615973301,\n          1.0,\n          0.5000078290910674\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"mnth\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6142.184250617928,\n        \"min\": 1.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          6.537775476149376,\n          7.0,\n          17379.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hr\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6140.496148184536,\n        \"min\": 0.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          11.546751826917545,\n          12.0,\n          17379.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"holiday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6144.34398083374,\n        \"min\": 0.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.028770355026181024,\n          1.0,\n          0.16716527638435244\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"weekday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6143.394057236404,\n        \"min\": 0.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          3.003682605443351,\n          3.0,\n          17379.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"workingday\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6144.194876084176,\n        \"min\": 0.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.6827205247712756,\n          1.0,\n          0.46543063352387354\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"weathersit\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6143.845618830189,\n        \"min\": 0.6393568777543036,\n        \"max\": 17379.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          17379.0,\n          1.425283387997008,\n          4.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"temp\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6144.242275843299,\n        \"min\": 0.02,\n        \"max\": 17379.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          0.4969871684216583,\n          0.5,\n          17379.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"atemp\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6144.248469131704,\n        \"min\": 0.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          0.4757751021347604,\n          0.4848,\n          17379.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hum\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6144.216991945488,\n        \"min\": 0.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          0.6272288394038783,\n          0.63,\n          17379.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"windspeed\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6144.317742909861,\n        \"min\": 0.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          0.1900976063064618,\n          0.194,\n          17379.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"casual\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6119.284233238239,\n        \"min\": 0.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          35.67621842453536,\n          17.0,\n          17379.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"registered\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6072.038722856437,\n        \"min\": 0.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          153.78686920996606,\n          115.0,\n          17379.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"cnt\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6060.617601280442,\n        \"min\": 1.0,\n        \"max\": 17379.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          189.46308763450142,\n          142.0,\n          17379.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 69
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Cleaning **data**\n"
      ],
      "metadata": {
        "id": "DPhVtPBhvb6D"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "day_df.drop_duplicates(inplace=True)"
      ],
      "metadata": {
        "id": "VYREyYWxuusG"
      },
      "execution_count": 71,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Jumlah duplikasi: \", day_df.duplicated().sum())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KkDQIRM8v0Da",
        "outputId": "804fee2b-eea4-4738-b59b-3c652eac9308"
      },
      "execution_count": 72,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Jumlah duplikasi:  0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "hour_df.drop_duplicates(inplace=True)"
      ],
      "metadata": {
        "id": "svbcMgp_wRv1"
      },
      "execution_count": 73,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Jumlah duplikasi: \", hour_df.duplicated().sum())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2sCEjHrfxd2U",
        "outputId": "8d3e48f8-8a24-41cd-e69e-0854b5c217b7"
      },
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Jumlah duplikasi:  0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Exploratory Data Analysis (EDA)"
      ],
      "metadata": {
        "id": "0abjwDz_vpEY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Menyaring kolom yang diperlukan dari day.csv dan hour.csv\n",
        "day_df_filtered = day_df[['instant', 'dteday', 'season', 'weathersit', 'cnt']]\n",
        "hour_df_filtered = hour_df[['instant', 'hr', 'season', 'weathersit', 'cnt']]\n",
        "\n"
      ],
      "metadata": {
        "id": "c709fd4QyWAE"
      },
      "execution_count": 75,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Menyaring data untuk analisis lebih lanjut (opsional)\n",
        "day_df_filtered['dteday'] = pd.to_datetime(day_df_filtered['dteday'])\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WLk2VZ1f6Aem",
        "outputId": "36d4267c-72f3-4505-b180-c2fd16786900"
      },
      "execution_count": 77,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-77-debbb5307d84>:2: SettingWithCopyWarning:\n",
            "\n",
            "\n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Menggabungkan data day.csv dan hour.csv berdasarkan 'instant'\n",
        "df_combined = pd.merge(day_df_filtered, hour_df_filtered, on='instant', suffixes=('_day', '_hour'))\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "SUlT30P-ylym"
      },
      "execution_count": 78,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_combined['cnt'] = df_combined['cnt_day'] + df_combined['cnt_hour']\n",
        "\n",
        "# Memeriksa kolom yang tersedia setelah penyesuaian\n",
        "print(df_combined.columns)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mrOzaoWG-z4U",
        "outputId": "e86ceada-24f2-48a9-c1f1-63a6c6402dc6"
      },
      "execution_count": 79,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['instant', 'dteday', 'season_day', 'weathersit_day', 'cnt_day', 'hr',\n",
            "       'season_hour', 'weathersit_hour', 'cnt_hour', 'cnt'],\n",
            "      dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Statistik deskriptif pada kolom 'cnt' yang menunjukkan jumlah penyewaan sepeda\n",
        "desc_stats = df_combined['cnt'].describe()\n",
        "print(desc_stats)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e4olv8dIJvn6",
        "outputId": "6151b626-06e3-4a19-890d-4c3a253af725"
      },
      "execution_count": 80,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "count     731.000000\n",
            "mean     4560.251710\n",
            "std      1936.964027\n",
            "min        24.000000\n",
            "25%      3229.000000\n",
            "50%      4591.000000\n",
            "75%      6009.000000\n",
            "max      8716.000000\n",
            "Name: cnt, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_combined['season'] = df_combined['season_day'] + df_combined['season_hour']\n",
        "\n",
        "# Memeriksa kolom yang tersedia setelah penyesuaian\n",
        "print(df_combined.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WfvreFBPKYSo",
        "outputId": "f12ed228-221b-4b26-f8db-c528a0a096ba"
      },
      "execution_count": 81,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['instant', 'dteday', 'season_day', 'weathersit_day', 'cnt_day', 'hr',\n",
            "       'season_hour', 'weathersit_hour', 'cnt_hour', 'cnt', 'season'],\n",
            "      dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "season_stats = df_combined.groupby('season')['cnt'].describe()"
      ],
      "metadata": {
        "id": "P-4U7SJ6K-mq"
      },
      "execution_count": 82,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_combined['weathersit'] = df_combined['weathersit_day'] + df_combined['weathersit_hour']\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "zGuwj4mLLGTh"
      },
      "execution_count": 83,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "weathersit_stats = df_combined.groupby('weathersit')['cnt'].describe()"
      ],
      "metadata": {
        "id": "9Yxi8Fh4L8y_"
      },
      "execution_count": 84,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Visualization & Explanatory Analysis"
      ],
      "metadata": {
        "id": "b2HoKbQo3JT8"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 85,
      "metadata": {
        "id": "gJr_9dXGpJ05"
      },
      "outputs": [],
      "source": [
        "# mengelompokan data berdasarkan'season' dan menghitung rata-rata penyewaan sepeda per musim\n",
        "season_avg = df_combined.groupby('season')['cnt'].mean()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Visualisasi pengaruh musim terhadap jumlah penyewaan sepeda\n",
        "plt.figure(figsize=(8, 6))\n",
        "sns.barplot(x=season_avg.index, y=season_avg.values, palette=\"viridis\")\n",
        "plt.title(\"Pengaruh Musim Terhadap Jumlah Penyewaan Sepeda\")\n",
        "plt.xlabel(\"Musim (1: Musim Semi, 2: Musim Panas, 3: Musim Gugur, 4: Musim Dingin)\")\n",
        "plt.ylabel(\"Rata-rata Penyewaan Sepeda\")\n",
        "plt.xticks(rotation=45)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 708
        },
        "id": "84fsmRkTNdce",
        "outputId": "26cc5cea-373a-4c65-fbff-2d35f7eb2fe2"
      },
      "execution_count": 86,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-86-11e766ae1963>:3: FutureWarning:\n",
            "\n",
            "\n",
            "\n",
            "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
            "\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsAAAAIlCAYAAADbpk7eAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAaXRJREFUeJzt3Xl0TPf/x/FXErIvlpJYIkIUsS8tsS9pU1LaUkotEara0lqKNl2iqEa11trqSy1FbVWtpYh9V0WspYo2aq2mEkISkvv7w8n8jFgyzAjm+Tgn52Q+9zP3vmfunckrn/ncOw6GYRgCAAAA7IRjThcAAAAAPEgEYAAAANgVAjAAAADsCgEYAAAAdoUADAAAALtCAAYAAIBdIQADAADArhCAAQAAYFcIwAAAALArBGDgIbNu3To5ODhowYIFOV3KfWnQoIEaNGiQ02Xct08++UQODg46f/68zbdVvHhxderUyebbedjc67Hy559/ysHBQV9++aX1iwIsZK+v30cVARg5btq0aXJwcDD9uLq66sknn1SPHj109uzZnC7vkXPj87lp06Ysyw3DkL+/vxwcHPT888/nQIXWkfmPQnZ+cGeZx8yvv/6a06U8UDcfQ7lz51aJEiXUsWNHHTt2LKfLs0t//vmnIiMjVbJkSbm6usrPz0/16tXTgAEDcro0PGZy5XQBQKZBgwYpMDBQKSkp2rRpkyZMmKBly5Zp//79cnd3z+nyHjmurq6aPXu26tSpY9a+fv16/f3333JxcbHp9leuXGnT9ZctW1bffvutWVtUVJQ8PT314Ycf2nTbeLy88847euqpp3T16lXt2rVLkyZN0tKlS7Vv3z4VLlw4p8uzG3/88Yeeeuopubm5qXPnzipevLhOnz6tXbt26fPPP9fAgQNzukQ8RgjAeGg0adJE1atXlyS99tpryp8/v0aMGKEff/xRbdu2zeHq7l1ycrI8PDwe+HabNm2q+fPna8yYMcqV6/9f6rNnz1a1atVs/pG+s7OzTdfv6+ur9u3bm7UNHTpUTzzxRJb2e3Ht2jVlZGTc93rw8Ktbt65efvllSVJkZKSefPJJvfPOO5o+fbqioqJyuDr7MXLkSF26dElxcXEKCAgwW3bu3LkcqgqPK6ZA4KHVqFEjSdLx48dNbTNnzlS1atXk5uamfPnyqU2bNjpx4oTZ/Ro0aKDy5cvr4MGDatiwodzd3VWkSBENGzYsyzb++usvNW/eXB4eHipYsKB69+6tFStWyMHBQevWrTP127hxo1q1aqVixYrJxcVF/v7+6t27t65cuWK2vk6dOsnT01NHjx5V06ZN5eXlpXbt2km6/fyw281/zMjI0JAhQ1S0aFG5urqqcePG+uOPP7L79Klt27b6999/FRsba2pLS0vTggUL9Oqrr2bpn/lx8I2PW/r/eZbTpk0ztZ05c0aRkZEqWrSoXFxcVKhQIb3wwgv6888/b/u4Mtc/b948DRw4UEWKFJGXl5defvllJSYmKjU1Vb169VLBggXl6empyMhIpaamZvvx3s6FCxfUq1cv+fv7y8XFRUFBQfr888/Nwu2Nc0lHjRqlkiVLysXFRQcPHjRbT6dOnZQnTx75+PgoMjJSly9fNtvW1KlT1ahRIxUsWFAuLi4KDg7WhAkTstRkGIY+/fRTFS1aVO7u7mrYsKEOHDiQpV9CQoL69u2rChUqyNPTU97e3mrSpIn27Nlj1i/zuZ07d64++OAD+fn5ycPDQ82bN8/y+siu2x2XnTp1UvHixU23b3zuxo0bpxIlSsjd3V3PPvusTpw4IcMwNHjwYBUtWlRubm564YUXlJCQcMdtp6WlKTo6WtWqVZOPj488PDxUt25drV279rb3mTRpkmm/PfXUU9qxY8c9PW7p1u89P//8s+rWrSsPDw95eXkpPDw8yz7LfP2fPHlSL774ojw9PVWgQAH17dtX6enpkq7v++LFi+uFF17Ist2UlBT5+PioW7duprbU1FQNGDBAQUFBpvee/v37m702WrRooapVq5qtq1mzZnJwcNBPP/1katu+fbscHBz0888/S8r+8ZXd/XHjsXAv++Po0aMqWrRolvArSQULFszSZsk+OXbsmMLCwuTh4aHChQtr0KBBMgzDrG9GRoZGjRqlcuXKydXVVb6+vurWrZv+++8/s37Wfv0iZzACjIfW0aNHJUn58+eXJA0ZMkQff/yxWrdurddee03//POPvvrqK9WrV0+7d+9Wnjx5TPf977//9Nxzz6lFixZq3bq1FixYoPfee08VKlRQkyZNJF0fmW3UqJFOnz6tnj17ys/PT7Nnz77lH9n58+fr8uXLevPNN5U/f3798ssv+uqrr/T3339r/vz5Zn2vXbumsLAw1alTR19++eU9T98YOnSoHB0d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3Vpbt27VihUrsiy7cOHCfc0vvtmtjpPExERNnTrVrF9oaKhy586tr776yqzvzeEnc503H+/z58+/7fzZGTNm6OLFi6bbCxYs0OnTp01XAbFEyZIldejQIf3zzz+mtj179mjz5s0Wr8tSt3out2/frq1bt9p82zcLCwuTt7e3PvvsM7OP/jPd+PxYqkOHDjp48KD69esnJycntWnTxmx569atdfLkySzvSZJ05coVJScnm27XqFFDuXPn1ueff658+fKpXLlykq4H423btmn9+vVmo79S9o+vB7U/Nm7ceMvnOHMOe+bo+L3sk7Fjx5p+NwxDY8eOVe7cudW4cWNJ15/r9PR0DR48OMt9r127ZhoYsOXrFw8WI8B4JJQsWVKffvqpoqKi9Oeff+rFF1+Ul5eXjh8/rh9++EGvv/66+vbta9E6u3XrprFjx6pt27bq2bOnChUqpFmzZsnV1VXS/08JKFOmjEqWLKm+ffvq5MmT8vb21vfff2/xCWCvvfaaFixYoOeee06tW7fW0aNHNXPmTNNohi1FRETctY+Pj49atWqlr776Sg4ODipZsqSWLFmSZZ7s77//rsaNG6t169YKDg5Wrly59MMPP+js2bNZ/oDntH79+umnn37S888/r06dOqlatWpKTk7Wvn37tGDBAv35559WG4l59tln5ezsrGbNmqlbt266dOmS/ve//6lgwYKmkStJpuvCxsTE6Pnnn1fTpk21e/du/fzzz1lqef755zVo0CBFRkaqVq1a2rdvn2bNmnXbTwzy5cunOnXqKDIyUmfPntWoUaMUFBR0yxM776Zz584aMWKEwsLC1KVLF507d04TJ05UuXLlzE78s4Xnn39eCxcu1EsvvaTw8HAdP35cEydOVHBwsC5dumTTbd/M29tbEyZMUIcOHVS1alW1adNGBQoUUHx8vJYuXaratWubhStLhIeHK3/+/Jo/f76aNGmSZf5phw4dNG/ePL3xxhtau3atateurfT0dB06dEjz5s3TihUrTKOj7u7uqlatmrZt22a6BrB0fQQ4OTlZycnJWQJwdo+vB7U/Pv/8c+3cuVMtWrQwfWqxa9cuzZgxQ/ny5TOdaGbpPnF1ddXy5csVERGhGjVq6Oeff9bSpUv1wQcfmKY21K9fX926dVNMTIzi4uL07LPPKnfu3Dpy5Ijmz5+v0aNH6+WXX7bp6xcPFgEYj4z3339fTz75pEaOHGn6Skx/f389++yzZldyyC5PT0+tWbNGb7/9tkaPHi1PT0917NhRtWrVUsuWLU1BOHfu3Fq8eLHeeecdxcTEyNXVVS+99JJ69OihSpUqZXt7YWFhGj58uEaMGKFevXqpevXqWrJkid59912La7eVr776SlevXtXEiRPl4uKi1q1b64svvlD58uVNffz9/dW2bVutXr1a3377rXLlyqUyZcpo3rx5atmyZQ5Wn5W7u7vWr1+vzz77TPPnz9eMGTPk7e2tJ598UgMHDjS7asH9Kl26tBYsWKCPPvpIffv2lZ+fn958800VKFAgyxUuPv30U7m6umrixIlau3atatSooZUrVyo8PNys3wcffKDk5GTNnj1bc+fOVdWqVbV06VK9//77t6zhgw8+0N69exUTE6OLFy+qcePGGj9+/F2vRZ05SnXj3M2yZctqxowZio6OVp8+fRQcHKxvv/1Ws2fPzvJlKdbWqVMnnTlzRl9//bVWrFih4OBgzZw5U/Pnz7f5tm/l1VdfVeHChTV06FB98cUXSk1NVZEiRVS3bl1FRkbe83qdnZ31yiuvaPz48WYnv2VydHTUokWLNHLkSM2YMUM//PCD3N3dVaJECfXs2TPLdLDM0d4bv/7cz89PQUFB+uOPP7IE4OweXw9qf3zwwQeaPXu21q9fr1mzZuny5csqVKiQ2rRpo48//tjshDtL9omTk5OWL1+uN998U/369ZOXl5cGDBiQ5RrjEydOVLVq1fT111/rgw8+UK5cuVS8eHG1b9/edO1kyXavXzxYDsb9nGECPIZGjRql3r176++//1aRIkVyuhzgrtatW6eGDRtq/vz593SVjzFjxqhnz576448/HsgnEvh/vXv31pQpU3TmzJl7/tIc3F6nTp20YMGCB/7JAR5+zAGGXbv5q4xTUlL09ddfq1SpUoRf2I0dO3bIw8Pjll9BC9tJSUnRzJkz1bJlS8Iv8IAxBQJ2rUWLFipWrJgqV66sxMREzZw5U4cOHbrtpXCAx8n333+vdevWadasWXrttdfu6fJRsNy5c+e0atUqLViwQP/++6969uyZ0yUBdod3O9i1sLAwTZ48WbNmzVJ6erqCg4M1Z84cvfLKKzldGmBzffv21cWLF9WlSxeNHDkyp8uxGwcPHlS7du1UsGBBjRkzRpUrV87p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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "weather_avg = df_combined.groupby('weathersit')['cnt'].mean()"
      ],
      "metadata": {
        "id": "GO7N_K4BNp_s"
      },
      "execution_count": 87,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Visualisasi pengaruh cuaca terhadap jumlah penyewaan sepeda\n",
        "plt.figure(figsize=(8, 6))\n",
        "sns.barplot(x=weather_avg.index, y=weather_avg.values, palette=\"coolwarm\")\n",
        "plt.title(\"Pengaruh Cuaca Terhadap Jumlah Penyewaan Sepeda\")\n",
        "plt.xlabel(\"Kategori Cuaca\")\n",
        "plt.ylabel(\"Rata-rata Penyewaan Sepeda\")\n",
        "plt.xticks(rotation=45)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 708
        },
        "id": "wnosElFsN02N",
        "outputId": "d233c378-ff39-4361-86f2-e92a52e8f518"
      },
      "execution_count": 88,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-88-6f8a7ad14894>:3: FutureWarning:\n",
            "\n",
            "\n",
            "\n",
            "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
            "\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsAAAAIlCAYAAADbpk7eAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAXI1JREFUeJzt3Xl8THf////nJGSRSBAk1gihxF5aotaKxlYtSqkSsRSlJWqp69eGalXrKqpqqUtrabV2vSxF7UtFSypqr8sWtWtIBElIzu8P38zHCG2GGVHncb/d5nYz7/M+57zOnJl45p33OWMxDMMQAAAAYBIuOV0AAAAA8DARgAEAAGAqBGAAAACYCgEYAAAApkIABgAAgKkQgAEAAGAqBGAAAACYCgEYAAAApkIABgAAgKkQgIFH0MaNG2WxWLRw4cKcLsW0unbtKm9v74eyL4vFohEjRjyUfT1KSpUqpa5du9q9Hp8PPErM+vn9pyMA45Ewc+ZMWSwW68PDw0PlypVTv379dO7cuZwu7x/ryJEj6tWrl0qXLi0PDw/5+PjomWee0YQJE3T9+vWcLu++3PleudejVKlSOV3qI2/EiBGyWCy6ePFiTpfyUPHz5tGzZ88evfTSSwoMDJSHh4eKFSumJk2aaOLEiTldGh5TuXK6AOB2I0eOVFBQkFJSUrR161ZNmTJFP/zwg/bu3as8efLkdHn/KCtWrFC7du3k7u6uLl26qFKlSkpLS9PWrVs1ePBg7du3T9OmTcvpMu1Wv359ff311zZtPXr00NNPP63XXnvN2vawRm/xz8XPm0fDtm3b1KhRI5UsWVI9e/ZUQECATp48qe3bt2vChAl64403crpEPIYIwHikNGvWTDVr1pR0K9T4+flp3Lhx+u9//6uOHTvmcHX37+rVq/Ly8npo+zt27Jg6dOigwMBArV+/XkWKFLEu69u3r/73v/9pxYoVD60eRypdurRKly5t09a7d2+VLl1ar7766gNvPyUlRW5ubg+8HTz6HtefN/80o0aNkq+vr3bs2KF8+fLZLDt//nzOFIXHHlMg8Eh79tlnJd0KdJm++eYb1ahRQ56enipQoIA6dOigkydP2qzXsGFDVapUSfv371ejRo2UJ08eFStWTGPGjMmyjxMnTqhVq1by8vJS4cKFFRUVpdWrV8tisWjjxo3Wflu2bFG7du1UsmRJubu7q0SJEoqKisoylSBz7uiRI0fUvHlz5c2bV506dZJ07zmPDRs2VMOGDbO0Z2RkaNSoUSpevLg8PDzUuHFj/e9///vb123MmDFKTk7Wl19+aRN+MwUHB6t///6SpOPHj8tisWjmzJlZ+t05t+3EiRN6/fXX9cQTT8jT01N+fn5q166djh8/nmXdy5cvKyoqSqVKlZK7u7uKFy+uLl26WP/cnpaWpujoaNWoUUO+vr7y8vJSvXr1tGHDhr89vuw4deqUunXrJn9/f7m7u6tixYr66quvbPpkziWdO3eu3nnnHRUrVkx58uRRUlKSzXZefPFFeXt7q1ChQho0aJDS09NttvPJJ5+oTp068vPzk6enp2rUqHHX+ampqamKiopSoUKFlDdvXrVq1Up//PFHln7ZfZ0z/5S/efNm9erVS35+fvLx8VGXLl106dKl+3rdsvsezXzt5s+fr/fee0/FihVT3rx59dJLLykxMVGpqakaMGCAChcuLG9vb0VGRio1NfUv952QkKBBgwapcuXK8vb2lo+Pj5o1a6bdu3fftf/9fj7uxZk/b5KTk+Xl5WX93N3ujz/+kKurq0aPHm1tu3z5sgYMGKASJUrI3d1dwcHB+vjjj5WRkWHt8+STT6pNmzY226pcubIsFot+++03a9u8efNksVh04MABSdl/f2X3fNz+Xrif83HkyBFVrFgxS/iVpMKFC2dps+ecxMbGqk6dOvL09FRQUJCmTp2aZXupqakaPny4goODrT/bhwwZkuX96ujPL3IWI8B4pB05ckSS5OfnJ+nWSMG7776r9u3bq0ePHrpw4YImTpyo+vXra9euXTY/QC9duqSmTZuqTZs2at++vRYuXKihQ4eqcuXKatasmaRbI7PPPvuszpw5o/79+ysgIEDffvvtXUPYggULdO3aNfXp00d+fn765ZdfNHHiRP3xxx9asGCBTd+bN28qPDxcdevW1SeffHLff0796KOP5OLiokGDBikxMVFjxoxRp06d9PPPP//lesuWLVPp0qVVp06d+9rvvezYsUPbtm1Thw4dVLx4cR0/flxTpkxRw4YNtX//futxJicnq169ejpw4IC6deumJ598UhcvXtTSpUv1xx9/qGDBgkpKStL06dPVsWNH9ezZU1euXNGXX36p8PBw/fLLL6pWrdp913nu3DnVrl1bFotF/fr1U6FChbRy5Up1795dSUlJGjBggE3/999/X25ubho0aJBSU1OtI8Dp6ekKDw9XrVq19Mknn2jt2rUaO3asypQpoz59+ljXnzBhglq1aqVOnTopLS1Nc+fOVbt27bR8+XK1aNHC2q9Hjx765ptv9Morr6hOnTpav369zXJ7X+dM/fr1U758+TRixAgdOnRIU6ZM0YkTJ6zBxJlGjx4tT09Pvf322/rf//6niRMnKnfu3HJxcdGlS5c0YsQIbd++XTNnzlRQUJCio6Pvua2jR4/q+++/V7t27RQUFKRz587piy++UIMGDbR//34VLVrUpv/9fj7uxZk/b7y9vdW6dWvNmzdP48aNk6urq3Xd7777ToZhWH9Rvnbtmho0aKBTp06pV69eKlmypLZt26Zhw4bpzJkz+vTTTyVJ9erV03fffWfdTkJCgvbt2ycXFxdt2bJFVapUkXTrl/dChQqpQoUKkrL//npY5yMwMFAxMTHau3evKlWq9Jd97T0nzZs3V/v27dWxY0fNnz9fffr0kZubm7p16ybp1i9RrVq10tatW/Xaa6+pQoUK2rNnj8aPH6/ff/9d33//vXV7zvr8IocYwCNgxowZhiRj7dq1xoULF4yTJ08ac+fONfz8/AxPT0/jjz/+MI4fP264uroao0aNsll3z549Rq5cuWzaGzRoYEgyZs+ebW1LTU01AgICjLZt21rbxo4da0gyvv/+e2vb9evXjfLlyxuSjA0bNljbr127lqXu0aNHGxaLxThx4oS1LSIiwpBkvP3221n6BwYGGhEREVnaGzRoYDRo0MD6fMOGDYYko0KFCkZqaqq1fcKECYYkY8+ePVm2kSkxMdGQZLzwwgv37HO7Y8eOGZKMGTNmZFkmyRg+fLj1+d1eg5iYmCyvdXR0tCHJWLx4cZb+GRkZhmEYxs2bN22OzTAM49KlS4a/v7/RrVu3bNWeycvLy+Z17d69u1GkSBHj4sWLNv06dOhg+Pr6Wo8j83UuXbp0lmPLPI8jR460aa9evbpRo0YNm7Y7101LSzMqVapkPPvss9a2uLg4Q5Lx+uuv2/R95ZVX7vt1zvzc1KhRw0hLS7O2jxkzxpBk/Pe//82yndsNHz7ckGRcuHDB2mbve7RSpUo2++7YsaNhsViMZs2a2awfGhpqBAYG2rTdua+UlBQjPT3dps+xY8cMd3d3m/PwIJ8Pw8i5nzerV682JBkrV6602WaVKlVsXtv333/f8PLyMn7//Xebfm+//bbh6upqxMfHG4ZhGAsWLDAkGfv37zcMwzCWLl1quLu7G61atTJefvllm+23bt3a+jy776+HdT5+/PFHw9XV1XB1dTVCQ0ONIUOGGKtXr7Z5XxmGcV/nZOzYsda21NRUo1q1akbhwoWt2/76668NFxcXY8uWLTbbnDp1qiHJ+OmnnwzDcM7nFzmLKRB4pISFhalQoUIqUaKEOnToIG9vby1ZskTFihXT4sWLlZGRofbt2+vixYvWR0BAgMqWLZtl1Nbb29tmTqibm5uefvppHT161Nq2atUqFStWTK1atbK2eXh4qGfPnllq8/T0tP776tWrunjxourUqSPDMLRr164s/W8fIbxfkZGRNvNR69WrJ0k2x3CnzD/f582b94H3f6fbX4MbN27ozz//VHBwsPLly6dff/3VumzRokWqWrWqWrdunWUbmSOSrq6u1mPLyMhQQkKCbt68qZo1a9psy16GYWjRokV6/vnnZRiGzXslPDxciYmJWbYfERFhc2y36927t83zevXqZXn9b1/30qVLSkxMVL169Wz288MPP0iS3nzzTZt17xyNvnN7f/U6Z3rttdeUO3du6/M+ffooV65c1n06U5cuXWz2XatWLRmGYR1hu7395MmTunnz5j235e7uLheXW/8tpaen688//5S3t7eeeOKJux73/Xw+bvewf96EhYWpaNGimjNnjrVt7969+u2332zWXbBggerVq6f8+fPb7DssLEzp6enavHmzzfFmPt+yZYueeuopNWnSRFu2bJF0ayrF3r17rX2l7L+/Htb5aNKkiWJiYtSqVSvt3r1bY8aMUXh4uIoVK6alS5da+9l7TnLlyqVevXpZn7u5ualXr146f/68YmNjra91hQoVVL58eZttZk6HydymMz+/yBlMgcAjZdKkSSpXrpxy5colf39/PfHEE9YfwIcPH5ZhGCpbtuxd1739P2FJKl68eJY//+bPn99mbtyJEydUpkyZLP2Cg4OzbD8+Pl7R0dFaunRplvmViYmJNs9z5cql4sWL/83R/r2SJUvaPM+fP78k/eX8Th8fH0nSlStXHnj/d7p+/bpGjx6tGTNm6NSpUzIMw7rs9tfgyJEjatu27d9ub9asWRo7dqwOHjyoGzduWNuDgoLuu8YLFy7o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Tp06pYyMDC1evFiHDh3S7NmztXz5cmfUCAAAADiM3SPAL7zwgpYtW6a1a9fKy8tL0dHROnDggJYtW6YmTZo4o0YAAADAYeweAZakevXqac2aNY6uBQAAAHC6+wrAmVJSUjRv3jxdu3ZNYWFhKlu2rKPqAgAAAJwi2wF44MCBunHjhiZOnChJSktLU+3atbV//37lyZNHgwcP1po1axQaGuq0YgEAAIAHle05wD/++KPNHN85c+YoPj5ehw8f1qVLl9SuXTt98MEHTikSAAAAcJRsB+D4+HiFhIRYn//444966aWXFBgYKIvFov79+2vXrl1OKRIAAABwlGwHYBcXFxmGYX2+fft21a5d2/o8X758unTpkmOrAwAAABws2wG4QoUKWrZsmSRp3759io+PV6NGjazLT5w4IX9/f8dXCAAAADhQti+CGzJkiDp06KAVK1Zo3759at68uYKCgqzLf/jhBz399NNOKRIAAABwlGyPALdu3Vo//PCDqlSpoqioKM2bN89meZ48efT66687vEAAAADAkey6D3Djxo3VuHHjuy4bPny4QwoCAAAAnMnur0IGAAAA/skIwAAAADAVAjAAAABMhQAMAAAAU8nRADxlyhRVqVJFPj4+8vHxUWhoqFauXGldnpKSor59+8rPz0/e3t5q27atzp07Z7ON+Ph4tWjRQnny5FHhwoU1ePBg3bx506bPxo0b9eSTT8rd3V3BwcGaOXPmwzg8AAAAPILsDsDnzp1T586dVbRoUeXKlUuurq42D3sUL15cH330kWJjY7Vz5049++yzeuGFF7Rv3z5JUlRUlJYtW6YFCxZo06ZNOn36tNq0aWNdPz09XS1atFBaWpq2bdumWbNmaebMmYqOjrb2OXbsmFq0aKFGjRopLi5OAwYMUI8ePbR69Wp7Dx0AAACPAbtugyZJXbt2VXx8vN59910VKVJEFovlvnf+/PPP2zwfNWqUpkyZou3bt6t48eL68ssv9e233+rZZ5+VJM2YMUMVKlSwfg3zjz/+qP3792vt2rXy9/dXtWrV9P7772vo0KEaMWKE3NzcNHXqVAUFBWns2LGSbn2j3datWzV+/HiFh4ffd+0AAAD4Z7I7AG/dulVbtmxRtWrVHFpIenq6FixYoKtXryo0NFSxsbG6ceOGwsLCrH3Kly+vkiVLKiYmRrVr11ZMTIwqV65s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YAAAAJgK4+IAAAAwFQIwAAAATIUADAAAAFMhAAMAAMBUCMAAAAAwFQIwAAAATIUADAAmt3HjRlksFl2+fDmnSwGAh4IADADZ1LVrV7344os2bQsXLpSHh4fGjh2brW3MnDlT+fLlc3xxD6BOnTo6c+aMfH19/7Lfrl271K5dO/n7+8vDw0Nly5ZVz5499fvvvz+kSgHAMQjAAHCfpk+frk6dOmnKlCl66623crqc+3Ljxg25ubkpICBAFovlnv2WL1+u2rVrKzU1VXPmzNGBAwf0zTffyNfXV+++++5DrBgAHhwBGADuw5gxY/TGG29o7ty5ioyMtLaPGzdOlStXlpeXl0qUKKHXX39dycnJkm5NNYiMjFRiYqIsFossFotGjBghSUpNTdWgQYNUrFgxeXl5qVatWtq4caPNPv/zn/+oRIkSypMnj1q3bq1x48ZlGU2eMmWKypQpIzc3Nz3xxBP6+uuvbZZbLBZNmTJFrVq1kpeXl0aNGvW3UyCuXbumyMhINW/eXEuXLlVYWJiCgoJUq1YtffLJJ/riiy8k3X10+/vvv7cJ1keOHNELL7wgf39/eXt766mnntLatWtt1klNTdXQoUNVokQJubu7Kzg4WF9++aUkKT09Xd27d1dQUJA8PT31xBNPaMKECfc8TwBwNwRgALDT0KFD9f7772v58uVq3bq1zTIXFxd99tln2rdvn2bNmqX169dryJAhkm5NNfj000/l4+OjM2fO6MyZMxo0aJAkqV+/foqJidHcuXP122+/qV27dmratKkOHz4sSfrpp5/Uu3dv9e/fX3FxcWrSpIlGjRpls+8lS5aof//+euutt7R371716tVLkZGR2rBhg02/ESNGqHXr1tqzZ4+6dev2t8e7evVqXbx40Xocd7JnSkdycrKaN2+udevWadeuXWratKmef/55xcfHW/t06dJF3333nT777DMdOHBAX3zxhby9vSVJGRkZKl68uBYsWKD9+/crOjpa//rXvzR//vxs1wAAMgAA2RIREWG4ubkZkox169Zla50FCxYYfn5+1uczZswwfH19bfqcOHHCcHV1NU6dOmXT3rhxY2PYsGGGYRjGyy+/bLRo0cJmeadOnWy2VadOHaNnz542fdq1a2c0b97c+lySMWDAAJs+GzZsMCQZly5duusxfPzxx4YkIyEh4S+P9W7HtmTJEuPv/qupWLGiMXHiRMMwDOPQoUOGJGPNmjV/uc7t+vbta7Rt2zbb/QGAEWAAsEOVKlVUqlQpDR8+3Dq14XZr165V48aNVaxYMeXNm1edO3fWn3/+qWvXrt1zm3v27FF6errKlSsnb29v62PTpk06cuSIJOnQoUN6+umnbda78/mBAwf0zDPP2LQ988wzOnDggE1bzZo17TpmwzDs6v9XkpOTNWjQIFWoUEH58uWTt7e3Dhw4YB0BjouLk6urqxo0aHDPbUyaNEk1atRQoUKF5O3trWnTptmMIAPA3yEAA4AdihUrpo0bN+rUqVNq2rSprly5Yl12/PhxtWzZUlWqVNGiRYsUGxurSZMmSZLS0tLuuc3k5GS5uroqNjZWcXFx1seBAwecMr/Vy8vLrv7lypWTJB08ePAv+7m4uGQJyzdu3LB5PmjQIC1ZskQffvihtmzZori4OFWuXNn6+nh6ev7lPubOnatBgwape/fu+vHHHxUXF6fIyMi/fH0B4E4EYACwU2BgoDZt2qSzZ8/ahODY2FhlZGRo7Nixql27tsqVK6fTp0/brOvm5qb09HSbturVqys9PV3nz59XcHCwzSMgIECS9MQTT2jHjh026935vEKFCvrpp59s2n766SeFhIQ80PE+99xzKliwoMaMGXPX5ZkXzxUqVEhXrlzR1atXrcvi4uKy1NO1a1e1bt1alStXVkBAgI4fP25dXrlyZWVkZGjTpk133ddPP/2kOnXq6PXXX1f16tUVHBxsHSUHgOwiAAPAfShRooQ2btyo8+fPKzw8XElJSQoODtaNGzc0ceJEHT16VF9//bWmTp1qs16pUqWUnJysdevW6eLFi7p27ZrKlSunTp06qUuXLlq8eLGOHTumX375RaNHj9aKFSskSW+88YZ++OEHjRs3TocPH9YXX3yhlStX2txhYfDgwZo5c6amTJmiw4cPa9y4cVq8eLH1Qrv75eXlpenTp2vFihVq1aqV1q5dq+PHj2vnzp0aMmSIevfuLUmqVauW8uTJo3/96186cuSIvv32W82cOdNmW2XLltXixYsVFxen3bt365VXXlFGRobN6xMREaFu3brp+++/17Fjx7Rx40brRW5ly5bVzp07tXr1av3+++969913s/wiAAB/K6cnIQPAP0VERITxwgsv2LT98ccfRtmyZY3atWsbiYmJxrhx44wiRYoYnp6eRnh4uDF79uwsF5j17t3b8PPzMyQZw4cPNwzDMNLS0ozo6GijVKlSRu7cuY0iRYoYrVu3Nn777TfretOmTTOKFStmeHp6Gi+++KLxwQcfGAEBATb1TJ482ShdurSRO3duo1y5csbs2bNtlksylixZYtP2dxfBZdqxY4fRpk0bo1ChQoa7u7sRHBxsvPbaa8bhw4etfZYsWWIEBwcbnp6eRsuWLY1p06bZXAR37Ngxo1GjRoanp6dRokQJ4/PPPzcaNGhg9O/f39rn+vXrRlRUlFGkSBHDzc3NCA4ONr766ivDMAwjJSXF6Nq1q+Hr62vky5fP6NOnj/H2228bVatW/cvaAeB2FsNw4NUNAICHpmfPnjp48KC2bNmS06UAwD9KrpwuAACQPZ988omaNGkiLy8vrVy5UrNmzdLkyZNzuiwA+MdhBBgA/iHat2+vjRs36sqVKypdurTeeOMN6/xbAED2EYABAABgKtwFAgAAAKZCAAYAAICpEIABAABgKgRgAAAAmAoBGAAAAKZCAAYAAICpEIABAABgKgRgAAAAmMr/D7sLUQKUqNA+AAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Memeriksa kolom yang tersedia setelah penyesuaian\n",
        "print(df_combined.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Fa8GBLjkP-3T",
        "outputId": "0b6847d2-4a03-421c-f349-5b2c48e6693f"
      },
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['instant', 'dteday', 'season_day', 'weathersit_day', 'cnt_day', 'hr',\n",
            "       'season_hour', 'weathersit_hour', 'cnt_hour', 'cnt', 'season',\n",
            "       'weathersit'],\n",
            "      dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(hour_df.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "51KKMl2KOiqq",
        "outputId": "e87c8ac3-8514-4df4-8b49-f3bba90c8ff1"
      },
      "execution_count": 90,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['instant', 'dteday', 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday',\n",
            "       'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed',\n",
            "       'casual', 'registered', 'cnt'],\n",
            "      dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2fhs6GZ4qFMx"
      },
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": 93,
      "metadata": {
        "id": "-gE-Ez1qtyIA"
      },
      "outputs": [],
      "source": [
        "# Memilih kolom yang ada di hour.csv\n",
        "hour_df_filtered = hour_df[['instant', 'hr', 'season', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt', 'mnth', 'season']]"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Menggabungkan data day.csv dengan hour.csv berdasarkan 'instant'\n",
        "df_combined = pd.merge(day_df[['instant', 'dteday', 'season', 'weathersit']], hour_df_filtered, on='instant', suffixes=('_day', '_hour'))\n",
        "\n",
        "print(df_combined.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YUd4bqq3RNw_",
        "outputId": "1a68cf95-2e8a-4261-8117-0f5150c45524"
      },
      "execution_count": 94,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['instant', 'dteday', 'season_day', 'weathersit_day', 'hr',\n",
            "       'season_hour', 'weathersit_hour', 'temp', 'atemp', 'hum', 'windspeed',\n",
            "       'casual', 'registered', 'cnt', 'mnth', 'season_hour'],\n",
            "      dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Korelasi antar kolom numerik yang ada dalam dataset gabungan\n",
        "corr_matrix = df_combined[['cnt', 'temp', 'atemp', 'hum', 'windspeed']].corr()\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "IV-EZL81RiDZ"
      },
      "execution_count": 96,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Visualisasi korelasi menggunakan heatmap\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.heatmap(corr_matrix, annot=True, cmap=\"coolwarm\", fmt=\".2f\", linewidths=0.5)\n",
        "plt.title(\"Heatmap Korelasi Antara Fitur-fitur Utama dan Penyewaan Sepeda\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 545
        },
        "id": "cNEQTjOXQxEu",
        "outputId": "dc90dab1-30e1-431e-89e1-69ca2b564d4c"
      },
      "execution_count": 97,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 2 Axes>"
            ],
            "image/png": "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wMPDA8+ePcvVRnBwMKZOnfqxoSv1SXUAek58UdQhUCHZ/FMJnL6TXNRhUCGp42+GsMePijoMKiSe3j7Yb1C6qMOgQtIm8z7qtvu7qMOgQnJqX4OiDkGpE7fStNp+w3LGWm2/sHEOABERERFRMcI5AERERESk0z6d8Sy6gRkAIiIiIqJihBkAIiIiItJpsk9oFSBdwAwAEREREVExwgwAEREREek0QWAGQBXsABARERGRTuMkYNVwCBARERERUTHCDAARERER6TSBk4BVwgwAEREREVExwgwAEREREek0GecAqIQZACIiIiKiYoQZACIiIiLSaVwGVDXMABARERERFSPMABARERGRTuN1AFTDDgARERER6TQZlwFVCYcAEREREREVI8wAEBEREZFO4xAg1TADQERERERUjDADQEREREQ6jcuAqoYZACIiIiKiYoQZACIiIiLSaTLOAVAJMwBERERERMUIMwBEREREpNO4CpBq2AEgIiIiIp0m8EJgKuEQICIiIiKiYoQZACIiIiLSaZwErBpmAIiIiIiIihFmAIiIiIhIp3ESsGqYASAiIiIiKkaYASAiIiIincYMgGqYASAiIiIiKkaYASAiIiIinSYTeB0AVajVAUhPT8fixYtx/PhxREdHQyaTKTx+5coVjQRHRERERPQhHAKkGrU6AAMGDMCRI0fQuXNnVK9eHSIRe11ERERERLpArQ7An3/+iQMHDqBOnTqajoeIiIiISCXMAKhGrUnArq6uMDc313QsRERERESkZWp1AObPn48JEybg2bNnmo6HiIiIiEglMkG7t8+NWkOAqlativT0dHh5ecHExAQGBgYKj8fHx2skOCIiIiIi0iy1OgA9evTAy5cv8eOPP8LR0ZGTgN/TuZkFGlUzhamxGA+eSrFmTwIi47LyrN++oTmqlTWGi4M+MjIFPHyWgd8PJiIiNuc5psYidG5mifK+EthZ6SMpJRuXbqdh+5EkpEk/w26pjgg9sA2H9mxAYkIc3Dx80Wvgd/AqVU5p3b+P7MKZE/vx8vljAIC7dxl81Wu4Qn1BELDn9xU4+ddupKYkw8evIvoMCYKjS8lC2R7K3959f2LHzp14/fo1vDw9MWzoNyhdurTSuqdOn8bWrdvwKiICWVlZcHV1QaeOndC0SWN5nY2/bcLfJ08iJiYGBgb68PHxQb8+feDn51dY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lt5QKBTw8/PD1q1bsXr1agBAv3798Prrr6OysvKhLQAPI5fLERwcjDlz5sDe3h7NmjXDxx9/rPFZ27VrF65cuYJ+/fpBoVDgP//5D9RqtUY3ofT0dMyePRtTpkxBXFwcvvrqK2k2oXbt2mHMmDEYN24cwsPDERAQgOzsbERFRcHPzw/Dhg3DvHnzEBgYiOnTpyMkJASWlpa4cOEC/vjjD6xevRpeXl4YMmQIpkyZgrVr18LIyAizZs3ilKekFX6TNKBPPvkE77//PhYuXAgfHx+MHj26zn0+e/XqhalTp2L06NFwdHTE8uXLGzhaepQPPvgAhoaGaN++PRwdHVFRUYHDhw9DpVJh8ODB8PX1xaxZs2Bra6uTH2nLli3DzJkz0aVLF9y8eRO//vqrdCWadMvAwADbt2/HqVOn0LFjR7z33ntYsWKFtN7IyAhffvklvvnmG7i4uOCll14CUD3t4Pr167Fx40b4+vpCqVRi06ZNOmkBGDhwINq2bYt+/fph9OjRePHFFzkd8BPg22+/RVVVFbp06YJZs2YhLCysqUPSK0qlEiqVSrrab2dnh/bt26N58+YaP8bra8WKFejbty9GjBiB5557Dn369NHoa29ra4udO3diwIAB8PHxwddff43vv/8eHTp0kMqMGzcOZWVl6N69O6ZNm4aZM2di8uTJ0vqNGzdi3LhxeP/99+Hl5YWRI0fixIkTaNWqFYDqcSMxMTFITk5G3759ERAQgIULF8LFxUVjHy4uLlAqlRg1ahQmT56MZs2aaX3cpL9k4t7OjETU5KKjo9G/f3/k5eVxcJeemjBhAvLz8/HLL780dShEVAdBQUHo1KkTVq1a1dShENUJWwCIiIiIiPQIEwAiIiIiIj3CLkBERERERHqELQBERERERHqECQARERERkR5hAkBEREREpEeYABARERER6REmAEREREREeoQJABERERGRHmECQERERESkR5gAEBERERHpESYARERERER65P8BFNbgrb1zqWAAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Mengelompokkan data berdasarkan jam ('hr') untuk melihat pola penyewaan sepeda per jam\n",
        "hour_avg = df_combined.groupby('hr')['cnt'].mean()\n",
        "\n"
      ],
      "metadata": {
        "id": "pZscW13SSfRL"
      },
      "execution_count": 98,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Visualisasi penyewaan sepeda per jam\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.lineplot(x=hour_avg.index, y=hour_avg.values, marker='o', color='green')\n",
        "plt.title(\"Penyewaan Sepeda Per Jam\")\n",
        "plt.xlabel(\"Jam\")\n",
        "plt.ylabel(\"Rata-rata Penyewaan Sepeda\")\n",
        "plt.xticks(range(0, 24, 1))\n",
        "plt.grid(True)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 564
        },
        "id": "V3HZA1LjS-ob",
        "outputId": "76854eeb-bb11-4afb-9ad3-5d4d6bd7b5d0"
      },
      "execution_count": 99,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1IAAAIjCAYAAAAJLyrXAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAtCpJREFUeJzs3Xd0lNX69vHvpBdS6CHU0EGqNOm9ihQrAhaO7afSDyJ4BAURjhwExO6xomA9iCi99yIdpPceSkhCElLnef/IOyORgBkyM88kuT5rsZaZtq9nEiH37L3vbTEMw0BERERERERyzMvsACIiIiIiInmNCikREREREREHqZASERERERFxkAopERERERERB6mQEhERERERcZAKKREREREREQepkBIREREREXGQCikREREREREHqZASERERERFxkAopERERD2OxWHj99dfNjiEiIrehQkpExAm+/PJLLBaL/U9AQABVq1Zl4MCBREdHmx2vQNqzZw8PPvgg5cuXJyAggNKlS9OxY0feffdds6O53Y0/m15eXkRGRtKpUydWrVrl8rFPnDiBxWJhypQpLh9LRMSdfMwOICKSn4wfP56oqCiSk5NZt24dH374IQsWLGDv3r0EBQWZHa/A2LBhA23btqVcuXI888wzREREcPr0aTZt2sQ777zDoEGDzI7odh07duTxxx/HMAyOHz/OBx98QLt27Zg/fz5du3Y1O56ISJ6jQkpExIm6du1Kw4YNAXj66acpWrQoU6dO5ZdffuHRRx81OV3B8eabbxIWFsbvv/9OeHh4lvsuXrxoTiiTVa1alf79+9u/7t27N3Xq1GH69Om5LqQSExMJDg7ObUQRkTxFS/tERFyoXbt2ABw/ftx+2zfffEODBg0IDAykSJEi9OnTh9OnT2d5Xps2bahVqxb79u2jbdu2BAUFUbp0aSZPnmx/TEJCAsHBwQwZMuSmcc+cOYO3tzeTJk2y3xYbG8vQoUMpW7Ys/v7+VK5cmbfeegur1Wp/zN13383999+f5bVq166NxWJh9+7d9tu+//57LBYL+/fvB+DkyZO88MILVKtWjcDAQIoWLcpDDz3EiRMnsrxWTEwMI0aMoHbt2hQqVIjQ0FC6du3Krl27sjxu1apVWCwWfvjhB958803KlClDQEAA7du358iRI7d9zwGOHj3KXXfddVMRBVCiRImb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//zzN+3teemll5g3bx7du3fnySefpEGDBiQmJrJnzx5++uknTpw4YZ8JqFy5MhERERw8eJBBgwbZX6NVq1a8/PLLADcVUt27d+frr78mLCyMmjVrsnHjRpYtW3bTPpXu3bszfvx4BgwYQLNmzdizZw+zZs2yz4g4y6BBg0hKSqJ3795Ur16d1NRUNmzYwPfff0+FChUYMGAA4Pj3JDIykrfeeosTJ05QtWpVvv/+e3bu3Mknn3xif88fe+wxfvjhB/7v//6PlStX0rx5czIyMjhw4AA//PADixcvpmHDhtSrV49HH32UDz74gLi4OJo1a8by5cuzPScrp+9vbrz//vu0aNGC2rVr88wzz1CxYkWio6PZuHEjZ86cuemMp9xw18+BiIgrqZASEXGjUaNGUbVqVaZNm8a4ceOAzD0znTp1okePHnf8uiVLlqRTp04sWLCAxx577Kb7g4KCWL16NRMnTuTHH39k5syZhIaGUrVqVcaNG5dlPxVkFko//vgjLVq0sN/WoEEDgoKCSE9Pp0mTJlke/8477+Dt7c2sWbNITk6mefPmLFu27Kb9Nq+88gqJiYnMnj2b77//nrvvvpv58+czatSoO7727EyZMoUff/yRBQsW8Mknn5Camkq5cuV44YUXePXVV7OcDeXI96Rw4cJ89dVXDBo0iP/+97+ULFmS9957j2eeecb+GC8vL+bOncu0adOYOXMmP//8M0FBQVSsWJEhQ4ZkWUL4+eefU7x4cWbNmsXcuXNp164d8+fPv2kfVU7f39yoWbMmW7duZdy4cXz55ZdcuXKFEiVKUL9+/Vydy2SbebpxKai7fg5ERFzJYmhHpohIvtC7d2/27NmT7YyG5F6bNm24fPkye/fuNTtKnrJ7927q1q3Lp59+ylNPPWV2HBERp9EeKRGRfOD8+fPMnz8/29koETP9/vvvQOaMl4hIfqKlfSIiedjx48dZv349n376Kb6+vlkOixUx08aNG1m5ciWTJ0+mWrVqNy0HFRHJ6zQjJSKSh61evZrHHnuM48eP89VXXxEREWF2JBEAPv74Y958803uuecefv31V/vB1CIi+YX2SImIiIiIiDhIHw+JiIiIiIg4SIWUiIiIiIiIg9RsArBarZw7d46QkBAsFovZcURERERExCSGYXDt2jUiIyNvu79ThRRw7ty5mw4/FBERERGRguv06dOUKVPmlverkAJCQkKAzDcrNDTU1CxpaWksWbKETp064evrWyDG1jUXjGs2c+yCeM1mjq1rLhjXbObYBfGazRy7IF6zmWPrmt17zdmJj4+nbNmy9hrhVlRIgX05X2hoqEcUUkFBQYSGhpryP48ZY+uaC8Y1mzl2QbxmM8fWNReMazZz7IJ4zWaOXRCv2cyxdc3mF1I2f7flR80mREREREREHKRCSkRERERExEEqpERERERERBykQkpERERERMRBKqREREREREQcpEJKRERERETEQSqkREREREREHKRCSkRERERExEEqpERERERERBykQkpERERERMRBKqREREREREQcpEJKRERERETEQSqkREREREREHKRCSkRERCSPCAkJMTuCiPx/KqREREREPFxiaiKGl0GNBjUwvAwSUxPNjiRS4KmQEhEREfFgyenJTF4/mZJTShI5PZKSU0oyecNkktOTzY4mUqD5mB1ARERERLKXmJrI5PWTGb9mvP222ORYxq/O/Hpks5EE+wWbFU+kQNOMlIiIiIiH8vX2ZcaWGdneN2PzDHy9fd2cSERsVEiJiIiIeKjY5Fhik2NveV9ccpx7A4mInQopEREREQ8VHhBOeED4Le8LCwhzbyARsVMhJSIiIuKh0jLSGNxkcLb3DW4ymLSMNDcnEhEbNZsQERER8VDBfsG83PxlrIaV97a8R2xyLOEB4QxsPJBh9wxTowkRE2lGSkRERMSDLTu2jAalGnB2+FnODTvH+X+e5+6Iu2n6WVN+OfCL2fFECiwVUiIiIiIebPWJ1fT+vjfjV41n/9b9eBvebDi9gQOXD/DUvKc4f+282RFFCiQVUiIiIiIebPuF7QBULlyZa9euATCh3QTqR9TnyvUrPPnLk1gNq5kRRQokFVIiIiIiHsowDHac3wFAvYh69tv9ffyZdf8sAn0CWXJ0Ce9sesekhCIFlwopEREREQ91PPY4cSlx+Hn7UbNYzSz31Sheg6mdpwIwavkodl3YZUZEkQJLhZSIiIiIh7LNRtUuURtfb9+b7n+uwXPcV/U+UjNS6TunL9fTrrs7okiBpUJKRERExENtP5+5P+ruUndne7/FYuGzHp9RMrgk+y7tY+TSke6MJ1KgqZASERER8VC2RhP1I+rf8jHFg4vzZa8vAXjv9/dYcHiBO6KJFHgqpEREREQ8kGEYfzsj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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# mengelompokan dan melihat pola penyewaan sepeda per bulan\n",
        "month_avg = df_combined.groupby('mnth')['cnt'].mean()"
      ],
      "metadata": {
        "id": "pvudAy41TFCw"
      },
      "execution_count": 100,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Visualisasi penyewaan sepeda per bulan\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.lineplot(x=month_avg.index, y=month_avg.values, marker='o', color='blue')\n",
        "plt.title(\"Penyewaan Sepeda Per Bulan\")\n",
        "plt.xlabel(\"Bulan\")\n",
        "plt.ylabel(\"Rata-rata Penyewaan Sepeda\")\n",
        "plt.xticks(range(1, 13, 1))\n",
        "plt.grid(True)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 564
        },
        "id": "4sH3CCtvTsch",
        "outputId": "9eb12596-e4a1-41fa-c667-defe452fa471"
      },
      "execution_count": 101,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1IAAAIjCAYAAAAJLyrXAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAYUZJREFUeJzt3Wl0FHX69vGrs5NACIRAEpYQCBB2VNQhgKhsioCiggIi4DKOqCwOIjwzrCoICuIKMjqMOCI7/tERNSwiCiiyCbKvgYAgOyEkhKSeFzEtTSqQgg7V6f5+zulDd3Wl+s5NPOai6neXwzAMQwAAAACAQvOzuwAAAAAAKG4IUgAAAABgEUEKAAAAACwiSAEAAACARQQpAAAAALCIIAUAAAAAFhGkAAAAAMAighQAAAAAWESQAgAAAACLCFIAALiRw+HQiBEj7C7Do3377bdyOBz69ttv7S4FAK4aQQqAz/vPf/4jh8PhfISEhKhmzZp69tlndfjwYbvL80kbN27Ugw8+qLi4OIWEhKhixYpq3bq13n77bbtLu+4u/tn08/NTbGys2rRpc11CyN69e10+3+FwKDw8XI0aNdI777yj7OzsIq8BADxVgN0FAICnGDVqlOLj45WRkaHvv/9ekyZN0pdffqlNmzYpNDTU7vJ8xooVK3THHXeoSpUqevLJJxUdHa39+/dr1apVevPNN/Xcc8/ZXeJ117p1az366KMyDEN79uzRe++9pzvvvFP/+9//dPfddxf553ft2lXt2rWTJJ06dUpffvmlnnvuOe3bt0+vvfZakX8+AHgighQA/OHuu+9W48aNJUlPPPGEIiMjNWHCBP3f//2funbtanN1vuOVV15R6dKltXr1akVERLi8d+TIEXuKslnNmjX1yCOPOF936tRJDRo00MSJE685SJ09e1ZhYWGX3efGG290+fw+ffro1ltv1fTp0wlSAHwWl/YBQAHuvPNOSdKePXuc2/773//qpptuUokSJVS2bFk9/PDD2r9/v8vX3X777apXr542b96sO+64Q6GhoapYsaLGjRvn3CctLU1hYWHq169fvs89cOCA/P39NWbMGOe2kydPqn///qpcubKCg4OVkJCgsWPHKicnx7nPjTfeqPvvv9/lWPXr15fD4dAvv/zi3DZz5kw5HA5t2bJFkrRv3z716dNHtWrVUokSJRQZGanOnTtr7969Lsc6fvy4Bg4cqPr166tkyZIKDw/X3XffrQ0bNrjsl7f+ZdasWXrllVdUqVIlhYSEqGXLltq5c+dley5Ju3btUt26dfOFKEkqX758vm1W/k7WrFmjpKQklShRQvHx8Zo8eXK+42VmZmr48OFKSEhQcHCwKleurEGDBikzMzPffgMGDFBUVJRKlSqljh076sCBA/mOV9j+WlG/fn2VK1fO5Wdz69atevDBB1W2bFmFhISocePGWrBggcvX5V3GumzZMvXp00fly5dXpUqVLH++w+FQhQoVFBAQkG+72fqwqlWrqlevXpc95vLly9W5c2dVqVLF2fcBAwbo3LlzLvv16tVLJUuWVGpqqu677z6VLFlSUVFRGjhwIJcaAriuOCMFAAXYtWuXJCkyMlJS7pmSoUOHqkuXLnriiSf0+++/6+2339Ztt92mdevWufzif+LECd111126//771aVLF82ZM0cvvvii6tevr7vvvlslS5ZUp06dNHPmTE2YMEH+/v7Or/30009lGIa6d+8uSUpPT1eLFi2Umpqqp556SlWqVNGKFSs0ZMgQHTp0SBMnTpQkNW/eXJ9++qnzOMePH9evv/4qPz8/LV++XA0aNJCU+wtrVFSUateuLUlavXq1VqxYoYcffliVKlXS3r17NWnSJN1+++3avHmz87LG3bt367PPPlPnzp0VHx+vw4cP6/3331eLFi20efNmxcbGuvTv1VdflZ+fnwYOHKhTp05p3Lhx6t69u3788cfL9j0uLk4rV67Upk2bVK9evcvua/XvpF27durSpYu6du2qWbNm6emnn1ZQUJAee+wxSVJOTo46duyo77//Xn/9619Vu3Ztbdy4UW+88Ya2b9+uzz77zHm8J554Qv/973/VrVs3JSUlacmSJbrnnnvy1VjY/lpx4sQJnThxQgkJCZKkX3/9VU2bNlXFihU1ePBghYWFadasWbrvvvs0d+5cderUyeXr+/Tpo6ioKA0bNkxnz5694uelp6fr6NGjkqTTp09r4cKF+uqrrzRkyBDLtRdk9uzZSk9P19NPP63IyEj99NNPevvtt3XgwAHNnj3bZd/s7Gy1bdtWt956q15//XUtWrRI48ePV/Xq1fX000+7rSYAuCwDAHzc1KlTDUnGokWLjN9//93Yv3+/MWPGDCMyMtIoUaKEceDAAWPv3r2Gv7+/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tWzZMt8ZxYvFxcUpJydHu3btcjkLtW3btnz7Fra/V6tatWqScs/AFeZnxF0uXLggKXcCZZ4yZcrk+77Onz/v/DsryMaNG7V9+3Z99NFHevTRR53bk5OT3VcwALgZa6QAoBDuv/9++fv7a+TIkfnOqBiGoWPHjl31sXv06KFvvvlGEydOVGRkZL77AnXp0kUrV67U119/ne9rT5486fyFVvpzHdLYsWPVoEED55mt5s2ba/Hixfr5559dLuuTcv91/9Lv6e233853FsFsv9mzZ+dbf3Otli5danrWKm9dUl5wsfp3cuHCBb3//vvO1+fPn9f777+vqKgo3XTTTZJye52amqp//etf+T7/3Llzzgl3eX9Hb731lss+eRMUL1bY/l6t8uXL6/bbb9f7779vGlh+//13t3zOpT7//HNJUsOGDZ3bqlev7lyjl2fKlClX/F7zgv3FfTIMQ2+++aa7ygUAt+OMFAAUQvXq1fXyyy9ryJAh2rt3r+677z6VKlVKe/bs0fz58/XXv/5VAwcOvKpjd+vWTYMGDdL8+fP19NNP51vb88ILL2jBggVq3769evXqpZtuuklnz57Vxo0bNWfOHO3du9d5RighIUHR0dHatm2bnnvuOecxbrvtNr344ouSlC9ItW/fXh9//LFKly6tOnXqaOXKlVq0aFG+dU/t27fXqFGj1Lt3byUlJWnjxo365JNPnGdE3OW5555Tenq6OnXqpMTERJ0/f14rVqzQzJkzVbVqVfXu3VuS9b+T2NhYjR07Vnv37lXNmjU1c+ZMrV+/XlOmTHH2vEePHpo1a5b+9re/aenSpWratKmys7O1detWzZo1S19//bUaN26sRo0aqWvXrnrvvfd06tQpJSUlafHixab3ySpsf6/Fu+++q2bNmql+/fp68sknVa1aNR0+fFgrV67UgQMH8t3ry6q1a9fqv//9ryTpzJkzWrx4sebOnaukpCS1adPGud8TTzyhv/3tb3rggQfUunVrbdiwQV9//fUVz1gmJiaqevXqGjhwoFJTUxUeHq65c+ey5gmAZ7u+QwIBwPPkjYRevXr1FfedO3eu0axZMyMsLMwICwszEhMTjWeeecbYtm2bc58WLVoYdevWzfe1PXv2NOLi4kyP265dO0OSsWLFCtP3z5w5YwwZMsRISEgwgoKCjHLlyhlJSUnG66+/nm8seOfO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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Pengembangan Dashboard"
      ],
      "metadata": {
        "id": "WxP52QMTUI0L"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import plotly.express as px"
      ],
      "metadata": {
        "id": "mPXf0z1sURAt"
      },
      "execution_count": 102,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Visualisasi interaktif untuk pengaruh musim terhadap penyewaan sepeda\n",
        "fig1 = px.bar(season_avg, x=season_avg.index, y=season_avg.values,\n",
        "              labels={'x': 'Musim', 'y': 'Rata-rata Penyewaan Sepeda'},\n",
        "              title=\"Pengaruh Musim Terhadap Jumlah Penyewaan Sepeda\")\n",
        "fig1.update_layout(xaxis_title=\"Musim\", yaxis_title=\"Rata-rata Penyewaan Sepeda\")\n",
        "fig1.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "0gXpqKD1Uoxa",
        "outputId": "8e5fa905-cc0b-4a68-9201-1e7110c187a8"
      },
      "execution_count": 103,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"f89d2ece-8732-4443-a7ef-7ccb637d72dd\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"f89d2ece-8732-4443-a7ef-7ccb637d72dd\")) {                    Plotly.newPlot(                        \"f89d2ece-8732-4443-a7ef-7ccb637d72dd\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"season=%{x}\\u003cbr\\u003eRata-rata Penyewaan Sepeda=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#000001\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[2,3,4,5],\"xaxis\":\"x\",\"y\":[2659.292817679558,5052.358695652174,5697.468085106383,4783.449438202248],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Musim\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Rata-rata Penyewaan Sepeda\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Pengaruh Musim Terhadap Jumlah Penyewaan Sepeda\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('f89d2ece-8732-4443-a7ef-7ccb637d72dd');\n",
              "var x = new MutationObserver(function (mutations, observer) {{\n",
              "        var display = window.getComputedStyle(gd).display;\n",
              "        if (!display || display === 'none') {{\n",
              "            console.log([gd, 'removed!']);\n",
              "            Plotly.purge(gd);\n",
              "            observer.disconnect();\n",
              "        }}\n",
              "}});\n",
              "\n",
              "// Listen for the removal of the full notebook cells\n",
              "var notebookContainer = gd.closest('#notebook-container');\n",
              "if (notebookContainer) {{\n",
              "    x.observe(notebookContainer, {childList: true});\n",
              "}}\n",
              "\n",
              "// Listen for the clearing of the current output cell\n",
              "var outputEl = gd.closest('.output');\n",
              "if (outputEl) {{\n",
              "    x.observe(outputEl, {childList: true});\n",
              "}}\n",
              "\n",
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Visualisasi interaktif untuk pengaruh cuaca terhadap penyewaan sepeda\n",
        "fig2 = px.bar(weather_avg, x=weather_avg.index, y=weather_avg.values,\n",
        "              labels={'x': 'Kategori Cuaca', 'y': 'Rata-rata Penyewaan Sepeda'},\n",
        "              title=\"Pengaruh Cuaca Terhadap Jumlah Penyewaan Sepeda\")\n",
        "fig2.update_layout(xaxis_title=\"Kategori Cuaca\", yaxis_title=\"Rata-rata Penyewaan Sepeda\")\n",
        "fig2.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "jha7SwOBUwIm",
        "outputId": "826bedc8-0f9c-439d-c1e8-d656b182fd52"
      },
      "execution_count": 104,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"f84233a7-b11e-4d4b-be42-85f435c4150b\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"f84233a7-b11e-4d4b-be42-85f435c4150b\")) {                    Plotly.newPlot(                        \"f84233a7-b11e-4d4b-be42-85f435c4150b\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"weathersit=%{x}\\u003cbr\\u003eRata-rata Penyewaan Sepeda=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#000001\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[2,3,4,5,6],\"xaxis\":\"x\",\"y\":[4864.7655677655675,4454.161971830986,4364.048611111111,3722.3703703703704,3851.3333333333335],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Kategori Cuaca\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Rata-rata Penyewaan Sepeda\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Pengaruh Cuaca Terhadap Jumlah Penyewaan Sepeda\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('f84233a7-b11e-4d4b-be42-85f435c4150b');\n",
              "var x = new MutationObserver(function (mutations, observer) {{\n",
              "        var display = window.getComputedStyle(gd).display;\n",
              "        if (!display || display === 'none') {{\n",
              "            console.log([gd, 'removed!']);\n",
              "            Plotly.purge(gd);\n",
              "            observer.disconnect();\n",
              "        }}\n",
              "}});\n",
              "\n",
              "// Listen for the removal of the full notebook cells\n",
              "var notebookContainer = gd.closest('#notebook-container');\n",
              "if (notebookContainer) {{\n",
              "    x.observe(notebookContainer, {childList: true});\n",
              "}}\n",
              "\n",
              "// Listen for the clearing of the current output cell\n",
              "var outputEl = gd.closest('.output');\n",
              "if (outputEl) {{\n",
              "    x.observe(outputEl, {childList: true});\n",
              "}}\n",
              "\n",
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "5nIBnL-1VD0E"
      },
      "execution_count": 42,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pip install streamlit\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RhsvwCPSWKi4",
        "outputId": "bd1afa0a-b374-4135-d136-2f0fcc3a4d4f"
      },
      "execution_count": 105,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.11/dist-packages (1.43.1)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.1.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.25.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.12.2)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.5)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.29.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.1)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.1.31)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.23.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st"
      ],
      "metadata": {
        "id": "VpbPUC_QWPOG"
      },
      "execution_count": 106,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Judul Dashboard\n",
        "st.title(\"Dashboard Analisis Penyewaan Sepeda\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UB8U7Vh_Wxhp",
        "outputId": "b41cbf4f-c0ed-427a-e6ae-c04d034e4a83"
      },
      "execution_count": 107,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-03-09 14:17:57.695 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:17:57.701 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 107
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Deskripsi\n",
        "st.write(\"\"\"\n",
        "    Dashboard ini menampilkan analisis mengenai faktor-faktor yang mempengaruhi jumlah penyewaan sepeda,\n",
        "    seperti pengaruh musim, cuaca, dan faktor lainnya yang relevan.\n",
        "\"\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Odqo7dasXMo-",
        "outputId": "287aa699-c48f-4712-89ec-2ece3c7b526c"
      },
      "execution_count": 108,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-03-09 14:17:59.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:17:59.504 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:17:59.510 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:17:59.514 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Sidebar untuk memilih analisis\n",
        "st.sidebar.header(\"Pilih Analisis\")\n",
        "analysis_type = st.sidebar.selectbox(\n",
        "    \"Pilih Jenis Analisis\",\n",
        "    (\"Pengaruh Musim Terhadap Penyewaan\", \"Korelasi Antara Fitur-Fitur\")\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VgonpolRXOnR",
        "outputId": "830654c0-276e-401f-8cd5-967419e4aeea"
      },
      "execution_count": 109,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-03-09 14:18:08.251 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:18:08.253 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:18:08.254 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:18:08.255 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:18:08.257 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:18:08.258 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:18:08.259 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:18:08.260 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df_combined.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BUXSc6jnZIfz",
        "outputId": "9338d35e-5f97-4c0f-9ad7-81e8254496e3"
      },
      "execution_count": 110,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['instant', 'dteday', 'season_day', 'weathersit_day', 'hr',\n",
            "       'season_hour', 'weathersit_hour', 'temp', 'atemp', 'hum', 'windspeed',\n",
            "       'casual', 'registered', 'cnt', 'mnth', 'season_hour'],\n",
            "      dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Pastikan menggabungkan day dan hour dengan benar\n",
        "df_combined = pd.merge(day_df[['instant', 'dteday', 'season']], hour_df[['instant', 'casual', 'registered']], on='instant', how='inner')\n",
        "\n",
        "# Cek kolom setelah penggabungan\n",
        "print(df_combined.columns)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pGlbE3MeZdD9",
        "outputId": "bc81716b-63bc-486f-8705-88903a4891e2"
      },
      "execution_count": 111,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['instant', 'dteday', 'season', 'casual', 'registered'], dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Memeriksa nilai yang hilang dalam kolom 'season'\n",
        "print(df_combined['season'].isnull().sum())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X8zl5tmvZ0GM",
        "outputId": "96f76bca-ea37-40c7-b14b-d2f057713803"
      },
      "execution_count": 113,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if analysis_type == \"Pengaruh Musim Terhadap Penyewaan\":\n",
        "    # Analisis Pengaruh Musim\n",
        "    st.subheader(\"Pengaruh Musim Terhadap Jumlah Penyewaan Sepeda\")\n",
        "\n",
        "    # Menghitung rata-rata jumlah penyewaan per musim\n",
        "    season_avg = df_combined.groupby('season')['casual'].mean() + df_combined.groupby('season')['registered'].mean()\n",
        "\n",
        "    # Visualisasi Pengaruh Musim\n",
        "    plt.figure(figsize=(8, 6))\n",
        "    sns.barplot(x=season_avg.index, y=season_avg.values, palette=\"viridis\")\n",
        "    plt.title(\"Pengaruh Musim Terhadap Penyewaan Sepeda\")\n",
        "    plt.xlabel(\"Musim (1: Musim Semi, 2: Musim Panas, 3: Musim Gugur, 4: Musim Dingin)\")\n",
        "    plt.ylabel(\"Rata-rata Penyewaan Sepeda\")\n",
        "    plt.xticks(rotation=45)\n",
        "\n",
        "    # Menampilkan grafik\n",
        "    st.pyplot(plt)\n",
        "\n",
        "elif analysis_type == \"Korelasi Antara Fitur-Fitur\":\n",
        "    # Analisis Korelasi Antara Fitur\n",
        "    st.subheader(\"Korelasi Antara Fitur-Fitur dan Penyewaan Sepeda\")\n",
        "\n",
        "    # Menghitung korelasi antar kolom numerik\n",
        "    corr_matrix = df_combined[['cnt', 'temp', 'atemp', 'hum', 'windspeed']].corr()\n",
        "\n",
        "    # Visualisasi Heatmap Korelasi\n",
        "    plt.figure(figsize=(10, 6))\n",
        "    sns.heatmap(corr_matrix, annot=True, cmap=\"coolwarm\", fmt=\".2f\", linewidths=0.5)\n",
        "    plt.title(\"Heatmap Korelasi Antara Fitur-fitur dan Penyewaan Sepeda\")\n",
        "\n",
        "    # Menampilkan grafik\n",
        "    st.pyplot(plt)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7-qK8AzIX3pI",
        "outputId": "305018b1-25ba-459f-d72b-435bb662785a"
      },
      "execution_count": 137,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-03-09 14:57:41.025 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:57:41.027 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "<ipython-input-137-640fad3d4145>:10: FutureWarning:\n",
            "\n",
            "\n",
            "\n",
            "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
            "\n",
            "\n",
            "2025-03-09 14:57:41.105 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:57:41.379 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-03-09 14:57:41.380 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Y6-iFurKZzvq"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}