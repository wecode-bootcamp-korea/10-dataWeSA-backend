import json

from django.http import JsonResponse
from django.views import View

from daily.models import State
from .models import (
    Place,
    Mobility
)

class MobilityView(View):
    def get(self, request):
        try:
            value_list = list(Mobility.objects.select_relvalue_listted('stvalue_listte').values('visit_rate', 'state'))
            name_list=[]
            data_all=[]
            data_list=[]
            tmp_id=2
            for value in value_list:
                state_obj = State.objects.get(id=value['state'])
                if state_obj.name in name_list:
                    pass
                else:
                    name_list.append(state_obj.name)
                if state_obj.id != tmp_id:
                    data_all.append(data_list)
                    data_list=[]
                tmp_id = state_obj.id
                data_list.append(i['visit_rate'])
            state_data=[]
            for name, data in zip(name_list, data_all):
                dic={}
                dic={'name': name, 'data': data}
                state_data.append(dic)
            return JsonResponse(
                {
                    'series': state_data
                }, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)
