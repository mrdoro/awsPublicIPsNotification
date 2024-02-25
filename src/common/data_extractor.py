import json
from src.common.check_instances import check_public_ip

def prepare_payload(data):
    print("Payload received by prepare_payload: " + json.dumps(data))
    
    base_payload = {
        'event_name': data['detail']['eventName'],
        'account_id': data['account'],
        'region': data['region'],
        'time': data['time']
    }
    
    payloads = []
    
    if base_payload['event_name'] == 'RunInstances':
        instance_ids = [item['instanceId'] for item in data['detail']['responseElements']['instancesSet']['items']]
        for instance_id in instance_ids:
            payload = base_payload.copy()
            payload['instance_ids'] = [instance_id]
            eip = check_public_ip([instance_id])
            payload['eip'] = eip
            payloads.append(payload)
    elif base_payload['event_name'] == 'AllocateAddress':
        payload = base_payload.copy()
        payload['eip'] = data['detail']['responseElements']['publicIp']
        payload['instance_ids'] = None
        payloads.append(payload)
    
    return [json.dumps(p) for p in payloads]