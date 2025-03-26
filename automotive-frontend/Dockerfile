# Use official Node.js image
FROM node:18

# Set working directory
WORKDIR /app

# Copy only package.json and package-lock.json first
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the project files
COPY . .

# Build React app
RUN npm run build

CMD ["npm", "start"]