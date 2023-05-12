import requests


def ai_chat(prompt):
    host = "ec2-35-90-219-160.us-west-2.compute.amazonaws.com"
    port = 5000
    uri = f'http://{host}:{port}/api/v1/generate'

    context = "Below is an instruction that describes a task. Write a response that appropriately completes the request and, after response, please stop generation."
    p = f"{context}\n### Human:\n{prompt}\n### Assistant:\n"

    request = {
        'prompt': p,
        'stopping_strings': ["\n### Human:"],
        'max_new_tokens': 250,
        'do_sample': True,
        'temperature': 1.3,
        'top_p': 0.1,
        'typical_p': 1,
        'repetition_penalty': 1.18,
        'top_k': 40,
        'min_length': 0,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'skip_special_tokens': True,
    }

    response = requests.post(uri, json=request)

    if response.status_code == 200:
        result = response.json()['results'][0]['text']
        return result.strip()

    return ''
