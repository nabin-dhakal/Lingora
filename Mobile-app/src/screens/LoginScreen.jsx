import React, { useState } from 'react';
import { View, StyleSheet, Text, TextInput, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const LoginScreen = () => {
  const navigation = useNavigation();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login</Text>
      <View style={styles.loginform}>
        <TextInput 
          style={styles.input}
          placeholder='Email' 
          value={email} 
          keyboardType='email-address' 
          onChangeText={setEmail} 
        />
        <TextInput 
          style={styles.input}
          placeholder='Password' 
          value={password} 
          onChangeText={setPassword} 
          secureTextEntry={true} 
        />
        <TouchableOpacity 
          style={styles.button}
          onPress={() => navigation.navigate('Home')}
        >
          <Text style={styles.buttonText}>Login</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={()=> navigation.navigate('SignUp')}>
          <Text style={styles.linkText}>Don't have an account? Sign Up</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    marginTop: 80,
  },
  loginform: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 12,
    marginBottom: 12,
    width: '80%',
    borderRadius: 8,
    fontSize: 16,
  },
  button: {
    backgroundColor: '#6C63FF',
    padding: 14,
    borderRadius: 8,
    width: '80%',
    alignItems: 'center',
    marginTop: 8,
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 16,
  },
  linkText: {
    marginTop: 20,
    color: '#6C63FF',
  },
});


export default LoginScreen;