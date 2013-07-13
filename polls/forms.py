    """
    else:
        if request.method == 'POST':
            form = CustomForm(request.POST)
            if form.is_valid():
                p.choice_set.create(choice=CustomForm())
                selected_choice.votes += 1
                selected_choice.save()
                request.session['choice'] = selected_choice
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents the data from being posted twice if a
                # user hits the Back button. 
                return render(request, 'polls/results.html', {
                        'poll' : p,
                        'choice' : selected_choice,
                    })
            else:
                pass
