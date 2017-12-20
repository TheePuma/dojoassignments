class SessionsController < ApplicationController
  def new
    render login
  end
  def create
    log user in
    if authenticate true
      save user id to session 
  end
  def destroy
  end
end
