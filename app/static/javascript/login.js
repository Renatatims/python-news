// Login Function
async function loginFormHandler(event) {
    event.preventDefault();
  
    const email = document.querySelector('#emailInput').value.trim();
    const password = document.querySelector('#inputPassword').value.trim();
  
    if (email && password) {
      const response = await fetch('/api/users/login', {
        method: 'post',
        body: JSON.stringify({
          email,
          password
        }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      if (response.ok) {
        document.location.replace('/dashboard/');
      } else {
        alert(response.statusText);
      }
    }
  }

  // Signup function

  async function signupFormHandler(event) {
    event.preventDefault();
  
    const username = document.querySelector('#inputSignupUsername').value.trim();
    const email = document.querySelector('#inputSignupEmail').value.trim();
    const password = document.querySelector('#inputSignupPassword').value.trim();
  
    if (username && email && password) {
      const response = await fetch('/api/users', {
        method: 'post',
        body: JSON.stringify({
          username,
          email,
          password
        }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      if (response.ok) {
        document.location.replace('/dashboard/');
      } else {
        alert(response.statusText);
      }
    }
  }

  document.querySelector('.login-form').addEventListener('submit', loginFormHandler);

  document.querySelector('.signup-form').addEventListener('submit', signupFormHandler);