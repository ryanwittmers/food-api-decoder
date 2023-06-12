
document.addEventListener('DOMContentLoaded', () => {

    // Adds a class to the health grade pill based on the grade value.
    const healthGradePill = document.querySelector('.health-grade-pill');
    if (healthGradePill) {
      const grade = healthGradePill.textContent.trim();
      switch (grade) {
        case 'A':
          healthGradePill.classList.add('grade-a');
          break;
        case 'B':
          healthGradePill.classList.add('grade-b');
          break;
        case 'C':
          healthGradePill.classList.add('grade-c');
          break;
        case 'D':
          healthGradePill.classList.add('grade-d');
          break;
        case 'F':
          healthGradePill.classList.add('grade-f');
          break;
        default:
          break;
      }
    }
  });

