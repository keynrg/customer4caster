def shifting_plot(y_hat, y_test, scaler, specific_plot = -1):
  i = random.randint(0, y_hat.shape[0]-n_steps_out)
  end_index = n_steps_out
  position_start_index = 0
  
  plt.figure(figsize=(20,10))
  plt.plot(s_demand.inverse_transform(y_test.reshape(y_hat.shape[0], y_hat.shape[1]))[i], label = "Truth", marker = 'x', alpha = 0.1, color = 'orange', linewidth = 5)

  if(specific_plot == -1):
    while(end_index > 0):
      plt.plot(pd.Series(data = (y_hat.reshape(y_hat.shape[0],y_hat.shape[1])[i])[0:end_index], index = np.arange(n_steps_out)[position_start_index:n_steps_out] ), marker = '4')
      i+=1
      end_index-=1
      position_start_index += 1
  else:
    plt.plot(pd.Series(data = (y_hat.reshape(y_hat.shape[0],y_hat.shape[1])[i+specific_plot])[0:end_index-specific_plot], index = np.arange(n_steps_out)[position_start_index + specific_plot:n_steps_out] ), marker = '4')  
  
  
  plt.xticks(np.arange(n_steps_out), array([str(n) for n in range(1,n_steps_out+1)]))
  plt.xlabel("nth step in the future")
  plt.legend()
  plt.ylabel("kVA")
  plt.show()
