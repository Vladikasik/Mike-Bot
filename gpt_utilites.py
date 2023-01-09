import openai
import config

class GPT_utilities:
    
    def __init__(self):
        openai.api_key = config.openai_api_key
        
        self.char_to_token = 4 # approximatly four characters is 1 token
        self.default_gpt_config = {
            "model": "text-davinci-003",
            "temperature": 0.7,
            "max_length":200,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
        self.gpt_config = self.default_gpt_config.copy()
    
    def get_response(self, prompt, **kwargs):
        model, temperature, max_length, frequency_penalty, presence_penalty = kwargs.get("model"), kwargs.get("temperature"), kwargs.get("max_length"), kwargs.get("frequency_penalty"), kwargs.get("presence_penalty")
        response = openai.Completion.create(
            model=model if model else self.gpt_config['model'],
            prompt=prompt,
            temperature=temperature if temperature else self.gpt_config['temperature'],
            max_tokens=max_length if max_length else self.gpt_config['max_length'],
            frequency_penalty=frequency_penalty if frequency_penalty else self.gpt_config['frequency_penalty'],
            presence_penalty=presence_penalty if presence_penalty else self.gpt_config['presence_penalty']
        )
        return response['choices'][0]['text']