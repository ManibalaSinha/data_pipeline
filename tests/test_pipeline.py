from pipeline.processor import transform_post, validate_post 
def test_validate_transform(): 

in_rec = {"userId": "1", "id": "10", "title": "hi", "body": "hello"} assert validate_post(in_rec) 
out = transform_post(in_rec) 
assert out['post_id'] == 10 
assert out['user_id'] == 1 
assert 'title' in out 