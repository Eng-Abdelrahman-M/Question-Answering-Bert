#https://medium.com/saarthi-ai/build-a-smart-question-answering-system-with-fine-tuned-bert-b586e4cfa5f5
import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
import re

class Qanswer:
    def __init__(self) -> None:
        #Model
        self.model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

        #Tokenizer
        self.tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')


    def answer(self,paragraph, question):
        paragraphs = re.split('\n+',paragraph)
        answers = []

        for paragraph in paragraphs: 
            encoding = self.tokenizer.encode_plus(text=question,text_pair=paragraph)

            inputs = encoding['input_ids']  #Token embeddings
            sentence_embedding = encoding['token_type_ids']  #Segment embeddings
            tokens = self.tokenizer.convert_ids_to_tokens(inputs) #input tokens

            scores = self.model(input_ids=torch.tensor([inputs]), token_type_ids=torch.tensor([sentence_embedding]))
            start_logits = scores['start_logits']
            end_logits = scores['end_logits']
            start_index=torch.argmax(start_logits)
            end_index=torch.argmax(end_logits)
            if end_index > start_index:
                answer = ' '.join(tokens[start_index:end_index+1])
                answers.append(answer.replace(" ##",""))
        return "\n".join(answers)