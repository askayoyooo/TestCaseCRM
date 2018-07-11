from django.shortcuts import render

# Create your views here.


def tester(request):

    return render(request, 'tester/tester_index.html')


def test_leader(request):

    return render(request, 'testleader/tester_leader_index.html')


def team_leader(request):

    return render(request, 'teamleader/team_leader_index.html')