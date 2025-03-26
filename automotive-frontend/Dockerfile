# Use official Node.js image
FROM node:18

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN npm install

# Build React app
RUN npm run build

CMD ["npm", "start"]