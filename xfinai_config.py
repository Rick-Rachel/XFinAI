import pandas as pd

# seed
seed = 416

# data config
data_start_time = pd.to_datetime('2022-01-01')
futures_index_map = {
    'ic': 0,
    'ih': 1,
    'if': 2
}
time_freq = '1m'

# dataset config
train_size = 0.7
val_size = 0.2
test_size = 1 - train_size - val_size

# feature config
label = 'return'
label_time_lag = 1
corr_threshold = 0.8
null_percent = 0.1

# model config
model_config = {
    "rnn": {
        "epochs": 20,
        "batch_size": 64,
        "hidden_size": 128,
        "seq_length": 32,
        "weight_decay": 0.03699014272607559,
        "num_layers": 2,
        "learning_rate": 0.006264079267383521,
        "dropout_prob": 0.0049846528896436
    },
    "lstm": {"batch_size": 64,
             "hidden_size": 4,
             "seq_length": 32,
             "weight_decay": 0.09190719792818434,
             "num_layers": 16,
             "learning_rate": 0.02362264773512453,
             "dropout_prob": 0.10062393919712778,
             'output_size': 1,
             'epochs': 10},
    "gru": {"batch_size": 64,
            "hidden_size": 4,
            "seq_length": 32,
            "weight_decay": 0.09190719792818434,
            "num_layers": 16,
            "learning_rate": 0.02362264773512453,
            "dropout_prob": 0.10062393919712778,
            'output_size': 1,
            'epochs': 100},
    "gru_cls": {"batch_size": 64,
                "hidden_size": 4,
                "seq_length": 32,
                "weight_decay": 0.09190719792818434,
                "num_layers": 16,
                "learning_rate": 0.02362264773512453,
                "dropout_prob": 0.10062393919712778,
                'output_size': 2,
                'epochs': 20},
}

# feature config
data_loader_config = {'shuffle': False,
                      'drop_last': True,
                      'num_workers': 2,
                      'pin_memory': True
                      }

# PATH
raw_data_path = 'D:/projects/XFinAI/data/raw_data'
processed_data_path = 'D:/projects/XFinAI/data/data_processed'
featured_data_path = 'D:/projects/XFinAI/data/data_featured'
raw_data_profile_path = 'D:/projects/XFinAI/EDA/data_profiles/raw_data'
featured_data_profile_path = 'D:/projects/XFinAI/EDA/data_profiles/featured_data'
scaler_path = 'D:/projects/XFinAI/data/scaler/'
losses_path = 'D:/projects/XFinAI/result/losses'
inference_result_path = 'D:/projects/XFinAI/result/inference_result'
model_save_path = 'D:/projects/XFinAI/model_layer/trained_models'
