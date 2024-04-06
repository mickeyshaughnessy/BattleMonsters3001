from prompts import p_update_battle

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('battlemonsters3001')

#for object_summary in my_bucket.objects.filter(Prefix="active_battles/"):
for object_summary in my_bucket.objects.filter(Prefix=""):
    print(object_summary.key)

def hatch_egg(request):
    hatched_monster = {}
    return hatched_monster

def run_battles(req):
    battles = get_battles 
    p = p_update_battle % battle 
    #new_battle = execute_completion(
