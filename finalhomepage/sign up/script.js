document.addEventListener('DOMContentLoaded', () => {
    const signUpForm = document.querySelector('form');
    const apiUrl = 'http://localhost:3001/users'; // API endpoint for users

    signUpForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const firstName = document.getElementById('first_name').value.trim();
        const lastName = document.getElementById('last_name').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();

        if (firstName && lastName && email && password) {
            const newUser = {
                first_name: firstName,
                last_name: lastName,
                email: email,
                password: password // In a real-world application, you would hash this
            };

            try {
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(newUser)
                });

                if (!response.ok) throw new Error('Failed to sign up');
                
                alert('Sign up successful!');
                signUpForm.reset();
            } catch (error) {
                console.error('Error:', error);
                alert('Error signing up. Please try again.');
            }
        } else {
            alert('Please fill out all fields.');
        }
    });
});
