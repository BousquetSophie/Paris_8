# -*- coding: utf-8 -*-
"""IA_et_apprentissage_TP7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1smUMhgUvAVkGjKIgD8vf9I-yiVdbX1AQ
"""

!pip install datasets
!pip install transformers
!pip install accelerate

import torch
import torch.nn as nn
import transformers
from transformers import Trainer
from torchtext.vocab import GloVe
from datasets import Dataset, load_dataset

#glove = GloVe(name='6B', dim=50)


ds_list = load_dataset("glue", "sst2", split=["train", "validation"])
train_ds, val_ds = ds_list

#print(ds_list)
#print(ds_list[1][0])

class MyModel(torch.nn.Module):
  def __init__(self, num_classes, num_tokens, hidden_size, num_layers, padding_idx=0):
    super(MyModel,self).__init__()
    self.embedding_layer = torch.nn.Embedding(num_embeddings=num_tokens, embedding_dim=hidden_size, padding_idx=padding_idx)
    self.conv_layers = torch.nn.ModuleList(
        [torch.nn.Conv1d(in_channels=hidden_size, out_channels=hidden_size, kernel_size=5, padding='same') for _ in range(num_layers)]
    )
    self.classifier = torch.nn.Linear(in_features=hidden_size, out_features=num_classes)

  def forward(self, inputs):
    out_embed = self.embedding_layer(inputs)
    out_embed = out_embed.transpose(1,2)

    for layer in self.conv_layers:
      out_embed = layer(out_embed)
      out_embed = torch.nn.GELU()(out_embed)

    out_embed_summed = torch.sum(out_embed, axis=-1)
    output = self.classifier(out_embed_summed)

    return output

tokenizer = transformers.AutoTokenizer.from_pretrained("bert-base-cased")

test = tokenizer("Hello world")["input_ids"][1:-1]
print(tokenizer.tokenize("Hello world"))
print(test)

print(tokenizer.decode(test))

def preprocess(ds):
  def encode_batch(batch):
    pre_out = tokenizer(batch['sentence'], max_length=128, truncation='longest_first')
    return pre_out

  dataset = ds.map(encode_batch, batched=True)
  dataset = dataset.remove_columns([x for x in dataset.column_names if
                                   x not in ['label', 'input_ids']])
  return dataset

tokenized_train_ds = preprocess(train_ds)
tokenized_test_ds = preprocess(val_ds)
print(tokenized_train_ds[0])
print(tokenized_test_ds[0])

model = MyModel(num_classes=2, num_tokens=tokenizer.vocab_size, hidden_size=64, num_layers=5, padding_idx=0)

model(torch.tensor([[1,2,3,4,5], [5,6,7,8,9]]))

class CustomTrainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False):
        labels = inputs.get('labels')
        inputs = inputs.get('input_ids')

        outputs = model(inputs)
        loss = torch.nn.CrossEntropyLoss()(outputs, labels)

        return (loss, outputs) if return_outputs else loss

    def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys=None):

        with torch.no_grad():
            labels = inputs.get("labels").view(-1)
            logits = model(inputs.get("input_ids"))
            loss = torch.nn.CrossEntropyLoss()(logits, labels)

        return (loss, logits, labels)

def compute_metric_fn(p):
  predictions = p.predictions
  labels = p.label_ids

  return {"accuracy": (predictions.argmax(-1) == labels).mean()}

from transformers import TrainingArguments, DataCollatorWithPadding

training_args = TrainingArguments(
    output_dir = 'output_dir',
    learning_rate=.001,
    num_train_epochs=5,
    per_device_train_batch_size=64,
    per_device_eval_batch_size=500,
    evaluation_strategy='steps',
    eval_steps=200,
    remove_unused_columns=False,
    logging_steps=10,
    save_strategy='no'
)


trainer = CustomTrainer(
    model = model,
    args=training_args,
    train_dataset=tokenized_train_ds,
    eval_dataset=tokenized_test_ds,
    compute_metrics=compute_metric_fn,
    data_collator=transformers.DataCollatorWithPadding(tokenizer),
)

trainer.train()
